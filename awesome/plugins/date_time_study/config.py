#大佬如果想自定义自己课表请移步mon.py文件中的switch相关字典中去设置课表时间
#lesson.py主要存放课程函数，如果原有文件中没有您想要的课程，您可以自行手动添加，后续读取csv格式自动导课表功能还在开发中，敬请期待（咕咕咕）
GROUP_ID=569209282#这个是发送的群号（目前只能实现一个群
START_LESSON=45#（开始时间
END_LESSON=59#结束提醒时间
#简单说明一下，nonebot的定时计划任务略复杂（人菜）为了保证效率（懒得多写代码)于是我设置计划任务为每十分种触发一次任务，然后进行对所在时间的判断，如果刚好在上述时间，则进行提醒