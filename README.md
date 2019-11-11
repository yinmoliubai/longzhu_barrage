# longzhu_barrage
龙珠弹幕


### 第一步，找到龙珠弹幕的websocke接口
步骤如下：
- 在龙珠首页，随意进入一个直播间；
- 按F12，然后刷新网页，点击WS选项；
- 点击出现websocket接口，选择右边的Headers,查看完整的url。

![1.png](https://upload-images.jianshu.io/upload_images/14750449-5b1bec54e0dad010.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 第二步，分析接口
如上图所见，接口是拼接而成的，拼接的字段如下：

![2.png](https://upload-images.jianshu.io/upload_images/14750449-112b945b35d3ec1e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

如果你在多看看其他直播间的接口你就会发现，其中appId,roomId,token的数据是会变化的，那么这些数据都是怎么来的呢？
通过抓包发现，对一个url请求之后上述所需要的数据都会被返回。
![url_data.png](https://upload-images.jianshu.io/upload_images/14750449-fdf714ea9a073f1a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这个url中唯一变动的就是roomid数据了，所以我们需要先拿到roomid号。通过对当前页面的分析，roomid已经在当前页面的HTML中出现了，所以只需要将roomid匹配出来就好了。

新建getdata.py文件，获取websocket接口所需数据信息。




### 第三步，分析推送数据
点击Message,查看客户端与服务器端的数据交互，分析是如何保持通信连接的。

![3.png](https://upload-images.jianshu.io/upload_images/14750449-8c68f970b1b1d818.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



通过上图，可以看到是服务器进行的无脑数据推送，而客户端发送的信息最多的是一种类型的数据，这应该是就是维持长连接所需要的心跳包。而且如果细心的话就会发现心跳包里面的body所对应的值会出现在上一条服务器端发送的信息中，我们拿过来用就行了。



结果：

![4.png](https://upload-images.jianshu.io/upload_images/14750449-63c3ccdb62750c02.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

通过对比还发现了一个问题，收到的数据有时候会重复，那就只能在数据处理的时候去重了。
