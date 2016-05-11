简单的基于ta-lib的均线策略示例
策略简介，主要是基于分时线的close线跟MA之间的关系出信号，同时对信号有个简单的过滤逻辑，同时展示了怎么调用gmsdk来做仓位管理。订单管理并没有在代码中体现， 如果需要对委托订单的状态进行跟踪，还需要增加on_order_status函数，用来跟踪订单的执行状态。
策略逻辑： 用分时bar线的收盘价跟ma线之间的交叉关系发出信号，并根据配置做一个简单的信号过滤。 用一个数列配置下单量，在出信号后，根据已有持仓状态确定是否开仓，或者是继续加仓，或者是回调加仓，还是加仓次数达上限后主动平仓出场。
