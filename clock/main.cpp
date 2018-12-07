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
#include <QDateTime>
#include <QObject>
#include <QTimer>
#include <unistd.h>
#include <stdio.h>  
using namespace std;


QDateTime dt = QDateTime::currentDateTime();
QLabel* my_label[2];
QString str;


int main(int argc, char **argv){
    QApplication window(argc, argv);
    
    
    QWidget *mainwindow = new QWidget;
    
    
    
    QPalette Pal = mainwindow->palette();
    mainwindow->setAttribute(Qt::WA_TranslucentBackground, true);
    mainwindow->setStyleSheet("background-color : rgba(75,8,128,200);");
    Pal.setColor(QPalette::WindowText, "#F7FE2E");
    //mainwindow->setMaximumSize(1980,1020);
    //mainwindow->setMinimumSize(250,150);
    //mainwindow->resize(500,500);
    mainwindow->setAutoFillBackground(true);
    mainwindow->setPalette(Pal);
    mainwindow->setWindowFlags( Qt::FramelessWindowHint|Qt::WindowStaysOnTopHint);
    
    QDesktopWidget d;
    int width=d.width();
    
    
    mainwindow->setGeometry(width-170,0,170,100);
    
    for(int i=0;i<2;i++){
        if(i==0){
            str=dt.toString("yyyy/MM/dd");
        }
        else{
            str=dt.toString("hh:mm:ss");
        }
        my_label[i] = new QLabel(mainwindow);
        my_label[i]->setPalette(Pal);
        my_label[i]->setFrameStyle( QFrame::Panel | QFrame::Sunken );
        my_label[i]->setText(str);
        my_label[i]->setFont(QFont("",20,QFont::Bold));
        if(i==0){
            my_label[i]->setAlignment(Qt::AlignVCenter | Qt::AlignLeft);
        }
        else{
            my_label[i]->setAlignment(Qt::AlignVCenter | Qt::AlignHCenter);
        }
        my_label[i]->setGeometry(0,0+50*i,170,50);
    }
    
    mainwindow->show();
    
    while(true){
        QDateTime d = QDateTime::currentDateTime();
        QApplication::processEvents();
        str=d.toString("yyyy/MM/dd");
        my_label[0]->setText(str);
        str=d.toString("hh:mm:ss");
        my_label[1]->setText(str);
    }
    
    return window.exec();
}
