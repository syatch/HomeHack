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
QLabel* my_label;
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
    
    
    mainwindow->setGeometry(width-170,124,170,75);
    
    my_label = new QLabel(mainwindow);
    my_label->setPalette(Pal);
    my_label->setFrameStyle( QFrame::Panel | QFrame::Sunken );
    my_label->setText(str);
    my_label->setFont(QFont("",15,QFont::Bold));
    my_label->setAlignment(Qt::AlignVCenter | Qt::AlignHCenter);
    my_label->setGeometry(0,0,170,75);
    
    mainwindow->show();
    
    while(true){
        QApplication::processEvents();
        QFile file("./home_data/data.txt");
        if (!file.open(QIODevice::ReadOnly))//読込のみでオープンできたかチェック
        {
            return 0;
        }
        QTextStream in(&file);
        str = in.readLine(0);
        str.insert(6, QString("\n"));
        str.insert(13, QString("\n"));
        my_label->setText(str);
    }
    
    return window.exec();
}
