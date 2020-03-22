##绝对路径和相对路径
####1.绝对路径以斜线开头"/"，代表从根目录寻找
####2.相对路径以双斜杠开头"//"，代表可以从html中的任何一处开始寻找元素，多个相对路径定位一个元素时用双斜杠分开。例如：//input[@id='a']//input[@name='b']
##根据属性值定位元素
####1.格式：//标签名[@属性1='属性值1' and @属性2='属性值2']
####2.运算符包括：=、!=、<、>、<=、>=、or、and
##其它xpath选择器
####1.contains://标签名[contains(@属性名称, "属性值")]。例如：//input[contains(@id,"a")]--查找id属性中包含"a"的input标签
####2.starts_with:判断一个属性以什么开头，例如//input[starts_with(@name,'a')]--查找属性name值以a开头的input属性
####3.text:通过文本内容定位，例如//input[text()='请输入密码']
####4.ancestor:首先查找到在ancestor声明之前的那个元素，然后将这个元素设为顶端节点，最后查找这个节点内所有符合规则的元素,//div[@id='d']//ancestor::div--查找id为d的div标签下的所有div标签。
####5.following:用于定位已给的父类节点之后的元素。首先找到following声明之前的元素（following前面以双斜线隔开的元素），并将这个元素设置为顶端节点然后找到在这个节点之后的所有元素（与ancestor分开，ancestor是顶端节点里，following是顶端节点后）
####6.child:查找当前节点的所有子节点,举例：//nav[@class=‘fusion-main-menu’]//ul[@id=‘menu-main’]/child::li,同时，你还可以通过给定下标选择特定的li元素 li[1],li[2]
####7.preceding:查找当前节点之前的所有节点，假如我们要查找所有标签名为li的元素，首先我们选定最底部的元素，然后用preceding::li
####8.following-sibling:查找当前节点的之后的
####9.descendant:查找并返回当前元素的所有后代元素,举例：//nav[@class=‘fusion-main-menu’]//[@id=‘menu-main’]//descendant::li
####10.parent:返回当前节点的所有父类节点