//Copyright (c) Takashi Ito 2018
//Twitter: @syatchIT
//github: https://github.com/syatch
#include <QApplication>
#include <qfile.h>
#include <qtextstream.h>
#include <stdlib.h>
#include <qlabel.h>
#include <qwidget.h>
#include <qapplication.h>
#include <QDesktopWidget>
#include <QPixmap>
#include <string>

using namespace std;

char bash_sh[7][50]={
    "bash ./get_data/bash/news/news_main.sh",
    "bash ./get_data/bash/news/news_society.sh",
    "bash ./get_data/bash/news/news_science.sh",
    "bash ./get_data/bash/news/news_politics.sh",
    "bash ./get_data/bash/news/news_economy.sh",
    "bash ./get_data/bash/news/news_international.sh",
    "bash ./get_data/bash/weather/weather2.sh",
};



int bash(int num){
    if(system(bash_sh[num])<0){
        fprintf(stderr, "error:Error in bash.sh.\n");
    }
    return 0;
}

int main(int argc, char **argv)
{
    QApplication window(argc, argv);
    QWidget *mainwindow = new QWidget;
    QPalette Pal = mainwindow->palette();
    mainwindow->setAttribute(Qt::WA_TranslucentBackground, true);
    mainwindow->setStyleSheet("background-color : rgba(75,8,128,200);");
    Pal.setColor(QPalette::WindowText, "#F7FE2E");
    //mainwindow->setMaximumSize(1980,1020);
    mainwindow->setMinimumSize(250,150);
    //mainwindow->resize(500,720);
    mainwindow->setAutoFillBackground(true);
    mainwindow->setPalette(Pal);
    
    QDesktopWidget d;
    int height=d.height();
    //printf("%d\n",height);
    QStringList argV = QCoreApplication::arguments();
    int argnum=argV[1].toInt();
    bash(argnum);
    
    //引数が0~5:ニュースを表示
    if(argnum<6){
        QString str[11];//
        QFile file("./get_data/news_get.txt");

        if (!file.open(QIODevice::ReadOnly))//読込のみでオープンできたかチェック
        {
            return 0;
        }

        QTextStream in(&file);

        for(int i=0;i<11;i++){
            str[i] = in.readLine(0);
            int l = str[i].length();
            int s = l;
            if(i%3==1&&i!=1){
                for(int j=0;j<s/10;j++){
                    str[i].insert(28*j, QString("\n"));
                    s++;
                }
            }
            else{
            }
            if(i!=1){
                QLabel *my_label = new QLabel(mainwindow);
                my_label->setPalette(Pal);
                my_label->setFrameStyle( QFrame::Panel | QFrame::Sunken );
                my_label->setText(str[i]);
                if(i%3==1){
                    my_label->setAlignment(Qt::AlignVCenter | Qt::AlignLeft);
                }
                else{
                    my_label->setAlignment(Qt::AlignVCenter | Qt::AlignHCenter);
                }


                if(i==0){
                    my_label->setGeometry(50,10,400,50);
                }
                else if(i%3==1){
                    my_label->setGeometry(50,140+230*(i/3-1),400,150);
                }
                else if(i%3==2){
                    my_label->setGeometry(50,90+230*(i/3),400,50);
                }
                else{
                    my_label->setGeometry(50,60+230*(i/3-1),400,30);
                }
            }
            else{
            }
        }
        file.close();
    }

    //引数が6:天気を表示
    else if(argnum==6){
        QString str[51];//
        QString title[5]={"日付","天気","降水確率（％）","最高気温","最低気温"};
    
        QFile file("./get_data/weather_get.txt");

        if (!file.open(QIODevice::ReadOnly))//読込のみでオープンできたかチェック
        {
            return 0;
        }


        for(int i=4;0<=i;i--){
            QLabel *my_label = new QLabel(mainwindow);
            my_label->setPalette(Pal);
            my_label->setFrameStyle( QFrame::Panel | QFrame::Sunken );
            my_label->setText(title[i]);
            my_label->setAlignment(Qt::AlignVCenter | Qt::AlignLeft);

	    if(i==0){
	        my_label->setGeometry(500,height-180,100,40);
	    }
	    else if(i==1){
	        my_label->setGeometry(500,height-140,100,80);
	    }
     	    else{
                my_label->setGeometry(500,height-20*(5-i),100,20);
            }  
        }
    
    
        QTextStream in(&file);
        for(int i=0;i<44;i++){
            str[i] = in.readLine(0);
            //文字を挿入するプログラム
            int l = str[i].length();
            if(i==0){
                str[i].insert(l+1,QString("(気象庁のWebページより)"));
            }
            else if(1<=i&&i<=7){
                str[i].insert(l-1,QString("\n"));
            }
            else if(30<=i&&i<=43){
                str[i].insert(l+1,QString("℃"));
            }
            else{
            }
            if(i==29){
            }
            else{
                QLabel *my_label = new QLabel(mainwindow);
                my_label->setPalette(Pal);
                my_label->setFrameStyle( QFrame::Panel | QFrame::Sunken );
                my_label->setText(str[i]);
                my_label->setAlignment(Qt::AlignVCenter | Qt::AlignCenter);
    
        	if(i==0){
    	            my_label->setGeometry(500,height-200,800,20);
    	        }
                else if(1<=i&&i<=7){
                    my_label->setGeometry(500+100*i,height-180,100,40);
                }
                else if(8<=i&&i<=20&&i%2==0){
                    my_label->setGeometry(500+100*(i/2-3),height-140,100,40);
                }
                else if(9<=i&&i<=21&&i%2==1){
                    my_label->setGeometry(500+100*(i/2-3),height-100,100,40);
                    QImage *Image =new QImage();
                    char* url = str[i].toUtf8().data();
                    //char url[14]="./get_data/png/100.png";
                    Image->load(url);
                    QPixmap pMap = QPixmap::fromImage(*Image);
                    pMap = pMap.scaled(my_label->size());
                    my_label->setPixmap(pMap);
                }
                else if(22<=i&&i<=28){
                    my_label->setGeometry(500+100*(i-21),height-60,100,20);
                }
                else if(30<=i&&i<=36){
                    my_label->setGeometry(500+100*(i-29),height-40,100,20);
                }
                else if(37<=i&&i<=43){
                    my_label->setGeometry(500+100*(i-36),height-20,100,20);
                }
                else{
                }
            }
        }
        file.close();
    }
    else{
        printf("Not registrated.\n");
    }
    mainwindow->showFullScreen();
    return window.exec();
}
