
import speech_recognition as sr
#初始化录音器
r=sr.Recognizer()
#开启麦克风录音
with sr.Microphone() as source:
    print("请说话")
    audio1=r.listen(source)

try:
    #将录音转换为文本
    text=r.recognize_google(audio1,language="zh-CN")
    print("你说的是："+text)
    #判断控制命令
    if"嗨朱迪" in text:
        print("你好主人请问需要什么服务")
        with sr.Microphone() as source:
          audio2=r.listen(source)
          text=r.recognize_google(audio2,language="zh-CN")
          if"起来画画" in text:
           print("您说的是"+text)
           print("好的我马上起来画画")

          else:
           print("主人我不知道你想让我干嘛")
    else:
       print("朱迪还在睡觉")
except sr.UnknownValueError:
   print("主人我无法识别你说的话")


