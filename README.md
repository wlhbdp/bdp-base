# 大数据生态解决方案基础平台

1.1 base-search
    
    技术：java, db，es
    搜索系统 
    统一搜索入口，搜索nosql db、es、db的数据   
    
1.2 base-common

    技术：java, db, spring cloud
    公共系统
    属于公共系统抽离，提供基础公共服务
  
1.3 base-task
    
    
    任务管理系统
    场景1：数据分析的task管理
    场景2：跑数据的task管理
    场景3：定时task管理

1.4 base-canal

    数据binlog采集
    配置mysql binlog, 实时采集到kakfa队列，然后基于kafka队列做spark计算
    
1.5 base-spider

    基础爬虫系统
    提供基础爬虫服务：扩展为gold爬虫，store爬虫

1.6 base-dts
    
    封装数据传输系统，基于数据进行互传，暴露接口服务给其他服务调用
    基于dataX封装数据传输系统
    
1.7 base-alarm

    基于grafana、promethus做一个运维告警系统
    运维告警系统
    

1.8 base-apm

    基于skywalking搭建分布式应用调用追踪系统，用于系统调优和排查调用错误
    Skywalking 应用分布式监控系统

1.9 base-config
    
    统一配置中心，从这里获取配置
    apollo 配置中心
    
1.10 base-report
    
    扩展为gold、store的报表系统
    报表系统

1.11 架构图

1.12 集群
    (集群维护)


# 2、金铺数据分析 bdp-gold

2.1 个性化推荐系统 gold-recommender

2.2 日志收集系统 gold-logclient gold-logserver

2.3 人群画像系统 gold-profile

2.4 数据传输系统（删除)

2.5 实时计算系统

2.6 反作弊系统 gold-anti-fraud

2.7 多维度分析系统 gold-multianaly

2.8 商场系统 linjiashop
    
    埋点：
        前端埋点，后端起一个服务，实时消费kafka队列的消息，然后做流计算统计
        前端调用埋点api到后端上报到kafka数据一致，前端调用失败 后端上报失败，失败重传 数据格式校验
        android开发埋点：https://github.com/foolchen/AndroidTracker


# 3、店家数据分析 store-analyse

3.1 智能营销推荐分析

3.2 消费者画像分析

3.3 店家信誉声量分析

3.4 topN商品分析

3.5 累计评论分析

3.6 宝贝详情分析

3.7 增量销售数据分析

3.8 活动效果分析

3.9 爬虫系统

3.10 店家Dashboard系统


