import pyautogui as pg
import speech_recognition as sr
import cv2
import mediapipe as mp
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import os
import time
import math
import random

'''
 开始调用opencv库实现对手势的识别
'''


#不同的手势来按不同的按钮，不同的按钮弹出来以后出现不同的动态图
#1.不同手势实现不同的图片切换

#(1)获取摄像头
cap=cv2.VideoCapture(0)#获取电脑的摄像头
cap.set(3,1280)#读入图像的宽度
cap.set(4,720)#图像的高度


#(3)手势识别参数的设置
#接受手部关键点识别的方法，最小手部检测模块置信度0.8，最多检测两只手
detector=HandDetector(detectionCon=0.8,maxHands=2)

#小鱼的默认位置
#fishpos=[100,100]

#(4)处理视频流传输来的帧图像
while True:
    #(2)获取小鱼图片
    imgwater=cv2.imread('D:\\python\\the fish\\sky.png')
    imggrass=cv2.imread('D:\\python\\the fish\\grass.png')

    imgfish=cv2.imread('D:\\python\\the fish\\fish.png',cv2.IMREAD_UNCHANGED)
    imgfish1=cv2.imread('D:\\python\\the fish\\fish3.png',cv2.IMREAD_UNCHANGED)
#调整背景图片的大小
    imgwater=cv2.resize(imgwater,dsize=(1280,720))
#调整背景草地图片的大小
    imggrass=cv2.resize(imggrass,dsize=(1280,720))
#调整小鱼图片的大小
   
    imgfish=cv2.resize(imgfish,dsize=(100,100))
    imgfish1=cv2.resize(imgfish1,dsize=(100,100))
    #返回是否读取成功，以及读取后的帧图像
    success,img=cap.read()#每次执行就读取一帧

    #图片反转呈现镜像关系，用1来左右翻转一下
    img=cv2.flip(img,flipCode=1)

    #手部关键点的检测，返回每只手的信息和绘制以后的图像

    hands,img=detector.findHands(img,flipType=False)
    img=cv2.addWeighted(img,1,0,0,0)

    #(5)手部关键点的处理
    if hands:
        #检测到手才出现背景图片
        hand=hands[0] 
        fingers=detector.fingersUp(hand)
        img=cv2.addWeighted(img,0.4,imgwater,0.6,0)
       
        if fingers==[1,1,0,0,0]:
          #如果竖起食指就出现第一张图片，并且图片跟随手指移动
         lmList=hand['lmList']
         x,y,w,h=hand['bbox']
         #获取手部检测的第八个监测点，也就是食指
         fingertip=lmList[8][0],lmList[8][1]
            #获取小鱼的宽高
         h1,w1=imgfish.shape[0:2]

            #获取小鱼的中心坐标y，随着食指移动
         x1,y1=fingertip
        
         img=cvzone.overlayPNG(img,imgfish,(x1,y1))
       


        if fingers==[1,1,1,0,0]: 
          #如果竖起食指和中指，就调用不同的图片
         lmList=hand['lmList']
         x,y,w,h=hand['bbox']
         #获取手部检测的第八个监测点，也就是食指
         fingertip=lmList[12][0],lmList[12][1]
         h1,w1=imgfish1.shape[0:2]

         #获取小鱼的中心坐标y，随着食指移动
         x1,y1=fingertip
         img=cvzone.overlayPNG(img,imgfish1,(x1,y1))




        if fingers==[0,1,1,0,0]:
         #当竖起大拇指的时候会出现草地的背景
         img=cv2.addWeighted(img,0.6,imggrass,0.4,0)
         lmList=hand['lmList']
         x,y,w,h=hand['bbox']
         #获取手部检测的第八个监测点，也就是食指
         fingertip=lmList[12][0],lmList[12][1]
         h1,w1=imgfish1.shape[0:2]

            #获取小鱼的中心坐标y，随着食指移动
         x1,y1=fingertip
        
         img=cvzone.overlayPNG(img,imgfish1,(x1,y1))
         
    cv2.imshow('img',img)
    #每帧滞留1ms后就消失
    
    k=cv2.waitKey(1)
        #Esc键能退出程序
    if k&0XFF==27:
     break

#释放视频资源
cap.release()
cv2.destroyAllWindows()