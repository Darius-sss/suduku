游戏软件--解9*9数独

软件目的：
1- 为了学习软件界面的实现，即学习使用pyqt5
2- 完整的实现一款软件，而不仅仅只是写核心算法
3- 情人节礼物（通关之后有照片福利，仅适用作者于对象）

软件开发中整体流程以及遇到的问题和细节：

1-  安装pyinstaller 和 pywin32 两个库
	--ps: 库可能较大，容易由网络波动导致失败，可使用镜像源安装

2-  设计UI界面
	--ps：使用tableWidget控件，设置行列名称不显示，设置滚动条不显示，设置单元格大小，设置字体加粗等
	添加各种btn控件，添加信号和槽函数
	--ps：点击编辑工具栏“编辑信号和槽” 略微拖动btn 添加信号和槽函数
	将ui文件转换成py文件
	
3-  新开一个main.py文件，创建一个继承之前转换过来的py文件的类
	将之前设计的槽函数在main中实现
	--ps：开始可以只定义好，写一个pass

4-  将所有的代码都完成之后，考虑将其打包
	--图标问题--自己找一个图片转换成 ico格式（网上有免费的）
	--数据问题--正常打包成exe之后，发现无法执行，查明原因是数据文件没有在其中
	--两种解决方式：
		-一种直接将资源文件复制过来放在相应位置即可（代码中写相对路径就好）
		-一种是将资源文件也打包到exe文件中，具体方式：在执行pyinstaller生成的spec文件中加上资源路径的元组，具体如下
		a = Analysis(['D:\\Doc\\code\\LeetCode\\解数独\\main.py'],
             pathex=['C:\\Users\\Darius\\AppData\\Local\\Programs\\Python\\Python38\\Scripts'],
             binaries=[
			 ('D:\\Doc\\code\\LeetCode\\解数独\\ziyuan\\fuli.jpg', 'ziyuan'),   # 添加的第一个资源，前面是资源原始地址，后面是添加后的相对位置
			 ('D:\\Doc\\code\\LeetCode\\解数独\\ziyuan\\problem.txt', 'ziyuan')  # 添加的第二个资源
			 ],
             datas=[],
			 --这种解决方式，需要注意在代码读取文件的地址出进行修改--由于exe运行时解压的文件夹是随机生成的名称，因此需要动态获取，具体见代码
	然后使用pyinstaller main.spec 执行spec文件进行打包
	
		
		-- bug1 小屏幕会导致表格显示不全
	
	    self.table.resizeRowsToContents()    # 调整行使得自适应大小
        self.table.resizeColumnsToContents()   # 调整列使得自适应大小