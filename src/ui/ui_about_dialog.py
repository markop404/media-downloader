# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_dialogbZEfBQ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(367, 322)
        AboutDialog.setMinimumSize(QSize(367, 322))
        icon = QIcon()
        icon.addFile(u"icons/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AboutDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.appIconLabel = QLabel(AboutDialog)
        self.appIconLabel.setObjectName(u"appIconLabel")
        self.appIconLabel.setMaximumSize(QSize(65, 65))
        self.appIconLabel.setPixmap(QPixmap(u"icons/icon.png"))
        self.appIconLabel.setScaledContents(True)

        self.headerLayout.addWidget(self.appIconLabel)

        self.appNameLabel = QLabel(AboutDialog)
        self.appNameLabel.setObjectName(u"appNameLabel")
        font = QFont()
        font.setFamilies([u"Cantarell Extra Bold"])
        font.setPointSize(16)
        font.setBold(True)
        self.appNameLabel.setFont(font)
        self.appNameLabel.setMargin(4)

        self.headerLayout.addWidget(self.appNameLabel)


        self.verticalLayout.addLayout(self.headerLayout)

        self.horizontalSpacer1 = QSpacerItem(40, 2, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer1)

        self.tabWidget = QTabWidget(AboutDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.aboutTab = QWidget()
        self.aboutTab.setObjectName(u"aboutTab")
        self.verticalLayout_3 = QVBoxLayout(self.aboutTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.aboutLabel = QLabel(self.aboutTab)
        self.aboutLabel.setObjectName(u"aboutLabel")
        self.aboutLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.aboutLabel.setWordWrap(True)
        self.aboutLabel.setOpenExternalLinks(True)
        self.aboutLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.aboutLabel)

        self.tabWidget.addTab(self.aboutTab, "")
        self.linksTab = QWidget()
        self.linksTab.setObjectName(u"linksTab")
        self.horizontalLayout_4 = QHBoxLayout(self.linksTab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leftColumnButtonLayout = QVBoxLayout()
        self.leftColumnButtonLayout.setObjectName(u"leftColumnButtonLayout")
        self.websiteButton = QPushButton(self.linksTab)
        self.websiteButton.setObjectName(u"websiteButton")
        self.websiteButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.leftColumnButtonLayout.addWidget(self.websiteButton)

        self.whatsNewButton = QPushButton(self.linksTab)
        self.whatsNewButton.setObjectName(u"whatsNewButton")
        self.whatsNewButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.leftColumnButtonLayout.addWidget(self.whatsNewButton, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_4.addLayout(self.leftColumnButtonLayout)

        self.rightColumnButtonLayout = QVBoxLayout()
        self.rightColumnButtonLayout.setObjectName(u"rightColumnButtonLayout")
        self.donateButton = QPushButton(self.linksTab)
        self.donateButton.setObjectName(u"donateButton")
        self.donateButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.rightColumnButtonLayout.addWidget(self.donateButton)

        self.supportedWebsitesButton = QPushButton(self.linksTab)
        self.supportedWebsitesButton.setObjectName(u"supportedWebsitesButton")
        self.supportedWebsitesButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.rightColumnButtonLayout.addWidget(self.supportedWebsitesButton, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_4.addLayout(self.rightColumnButtonLayout)

        self.tabWidget.addTab(self.linksTab, "")
        self.disclaimerTab = QWidget()
        self.disclaimerTab.setObjectName(u"disclaimerTab")
        self.horizontalLayout_3 = QHBoxLayout(self.disclaimerTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.disclaimerLabel = QLabel(self.disclaimerTab)
        self.disclaimerLabel.setObjectName(u"disclaimerLabel")
        self.disclaimerLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.disclaimerLabel.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.disclaimerLabel)

        self.tabWidget.addTab(self.disclaimerTab, "")
        self.licenseTab = QWidget()
        self.licenseTab.setObjectName(u"licenseTab")
        self.horizontalLayout_2 = QHBoxLayout(self.licenseTab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.licenseBrowser = QTextBrowser(self.licenseTab)
        self.licenseBrowser.setObjectName(u"licenseBrowser")
        self.licenseBrowser.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.licenseBrowser)

        self.tabWidget.addTab(self.licenseTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.copyrightLabel = QLabel(AboutDialog)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setIndent(1)

        self.verticalLayout.addWidget(self.copyrightLabel)

        self.closeDialogButton = QPushButton(AboutDialog)
        self.closeDialogButton.setObjectName(u"closeDialogButton")
        self.closeDialogButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.closeDialogButton.setIcon(icon1)

        self.verticalLayout.addWidget(self.closeDialogButton, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(AboutDialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.appIconLabel.setText("")
        self.appNameLabel.setText(QCoreApplication.translate("AboutDialog", u"Media Downloader", None))
        self.aboutLabel.setText(QCoreApplication.translate("AboutDialog", u"<b>Web video / audio downloader</b><br>v4.0.0<br><br>Made by <a href=\"https://markopejic.com\">Marko Peji\u0107</a>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), QCoreApplication.translate("AboutDialog", u"About", None))
        self.websiteButton.setText(QCoreApplication.translate("AboutDialog", u"Website", None))
        self.whatsNewButton.setText(QCoreApplication.translate("AboutDialog", u"What's New", None))
        self.donateButton.setText(QCoreApplication.translate("AboutDialog", u"Donate", None))
        self.supportedWebsitesButton.setText(QCoreApplication.translate("AboutDialog", u"Supported Websites", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.linksTab), QCoreApplication.translate("AboutDialog", u"Links", None))
        self.disclaimerLabel.setText(QCoreApplication.translate("AboutDialog", u"The authors of Media Downloader are not responsible/liable for any misuse of this program that may violate local copyright/DMCA laws. Users use this application at their own risk.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.disclaimerTab), QCoreApplication.translate("AboutDialog", u"Disclaimer", None))
        self.licenseBrowser.setHtml(QCoreApplication.translate("AboutDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><title>GNU General Public License v3.0 - GNU Project - Free Software Foundation (FSF)</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<h3 align=\"center\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">GNU GENERAL PUBLIC LICENSE</span></h3>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Not"
                        "o Sans'; font-size:10pt;\">Version 3, 29 June 2007 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Copyright \u00a9 2007 Free Software Foundation, Inc. &lt;</span><a href=\"https://fsf.org/\"><span style=\" font-family:'Noto Sans'; font-size:10pt; text-decoration: underline; color:#00d3b8;\">https://fsf.org/</span></a><span style=\" font-family:'Noto Sans'; font-size:10pt;\">&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed. </span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"preamble\"></a><span style=\""
                        " font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">P</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">reamble </span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The GNU General Public License is a free, copyleft license for software and other kinds of works. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public Licens"
                        "e for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">To protect your rights, we need to prevent others from denying you these rights or asking you"
                        " to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">For example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Developers that use the GNU GPL protect your rights with two steps: (1) assert copyright on the software, and (2) offer you this License giving you legal p"
                        "ermission to copy, distribute and/or modify it. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">For the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software. For both users' and authors' sake, the GPL requires that modified versions be marked as changed, so that their problems will not be attributed erroneously to authors of previous versions. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so. This is fundamentally incompatible with the aim of protecting users' freedom to change the software. The systematic pattern of"
                        " such abuse occurs in the area of products for individuals to use, which is precisely where it is most unacceptable. Therefore, we have designed this version of the GPL to prohibit the practice for those products. If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL, as needed to protect the freedom of users. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Finally, every program is threatened constantly by software patents. States should not allow patents to restrict development and use of software on general-purpose computers, but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary. To prevent this, the GPL assures that patents cannot be used to render the program non-free. </span></p>\n"
"<p style"
                        "=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The precise terms and conditions for copying, distribution and modification follow. </span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"terms\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">T</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">ERMS AND CONDITIONS </span></h4>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section0\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">0</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">. Definitions. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">\u201cThis License\u201d refers to version 3 of the GNU General Public License. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">\u201cCopyright\u201d also means copyright-like laws that apply to other kinds of works, such as semiconductor masks. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">\u201cThe Program\u201d refers to any copyrightable work licensed under this License. Each licensee is addressed as \u201cyou\u201d. \u201cLicensees\u201d and \u201crecipients\u201d may be individuals or organizations. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">To \u201cmodify\u201d a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission, other than the making of an exact copy. The resulting work is called a \u201cmodified version\u201d of the earlier work or a work \u201cbased on\u201d the earlier work. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">A \u201ccovered work\u201d means either the unmodified Program or a work based on the Program. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">To \u201cpropagate\u201d a work means to do anything with it that, without permission, would make you directly or secondarily liable for infringement "
                        "under applicable copyright law, except executing it on a computer or modifying a private copy. Propagation includes copying, distribution (with or without modification), making available to the public, and in some countries other activities as well. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">To \u201cconvey\u201d a work means any kind of propagation that enables other parties to make or receive copies. Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">An interactive user interface displays \u201cAppropriate Legal Notices\u201d to the extent that it includes a convenient and prominently visible feature that (1) dis"
                        "plays an appropriate copyright notice, and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided), that licensees may convey the work under this License, and how to view a copy of this License. If the interface presents a list of user commands or options, such as a menu, a prominent item in the list meets this criterion. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">1</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">. Source Code. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The \u201csource code\u201d for a work means the preferred form of the work for making modifications to it. \u201c"
                        "Object code\u201d means any non-source form of a work. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">A \u201cStandard Interface\u201d means an interface that either is an official standard defined by a recognized standards body, or, in the case of interfaces specified for a particular programming language, one that is widely used among developers working in that language. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The \u201cSystem Libraries\u201d of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component, but which is not part of that Major Component, and (b) serves only to enable use of the work with that Major Component, or to"
                        " implement a Standard Interface for which an implementation is available to the public in source code form. A \u201cMajor Component\u201d, in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs, or a compiler used to produce the work, or an object code interpreter used to run it. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The \u201cCorresponding Source\u201d for a work in object code form means all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. However, it does not include the work's System Libraries, or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not pa"
                        "rt of the work. For example, Corresponding Source includes interface definition files associated with source files for the work, and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The Corresponding Source need not include anything that users can regenerate automatically from other parts of the Corresponding Source. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The Corresponding Source for a work in source code form is that same work. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-"
                        "bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section2\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">2</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">. Basic Permissions. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program. The output from running a covered work is covered by this License only if the output, given its content, constitutes a covered work. This License acknowledges your rights of fair use or other equivalent, as provided by copyright law. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">You may make, run and propagate covered works that you do not convey, without conditions so long as your license otherwise remains in force. You may convey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works, provided that you comply with the terms of this License in conveying all material for which you do not control copyright. Those thus making or running the covered works for you must do so exclusively on your behalf, under your direction and control, on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Conveying unde"
                        "r any other circumstances is permitted solely under the conditions stated below. Sublicensing is not allowed; section 10 makes it unnecessary. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section3\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">3</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">. Protecting Users' Legal Rights From Anti-Circumvention Law. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">No covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty adopted on 20 December 1996, or similar laws prohibiting or restricting circumvention of such measures. </span></p>\n"
"<p style=\""
                        " margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">When you convey a covered work, you waive any legal power to forbid circumvention of technological measures to the extent such circumvention is effected by exercising rights under this License with respect to the covered work, and you disclaim any intention to limit operation or modification of the work as a means of enforcing, against the work's users, your or third parties' legal rights to forbid circumvention of technological measures. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section4\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">4</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">. Conveying Verbatim Copies. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:1"
                        "2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">You may convey verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><a name=\"section5\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">5</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">. Conveying Modified Source Versions. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions: </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a) The work must carry prominent notices stating that you modifie"
                        "d it, and giving a relevant date. </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to \u201ckeep intact all notices\u201d. </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged. This License gives no permission to license the work in any other way, but it does not invalidate such permissio"
                        "n if you have separately received it. </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however, if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so. </li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, and which are not combined with it such as to form a larger program, in or on a volume of a storage or distribution medium, is called an \u201caggregate\u201d if the compilation and its resulting copyright are not used to limit the access or "
                        "legal rights of the compilation's users beyond what the individual works permit. Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section6\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">6</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">. Conveying Non-Source Forms. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">You may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this License, in one of these ways: </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0p"
                        "x; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by the Corresponding Source fixed on a durable physical medium customarily used for software interchange. </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by a written offer, valid for at least three years and valid for as long as you offer spare parts or customer support for that product model, to give anyone who possesses the object code either (1) a copy of the Corresponding Source for all the softwa"
                        "re in the product that is covered by this License, on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or (2) access to copy the Corresponding Source from a network server at no charge. </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c) Convey individual copies of the object code with a copy of the written offer to provide the Corresponding Source. This alternative is allowed only occasionally and noncommercially, and only if you received the object code with such an offer, in accord with subsection 6b. </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">d) Convey the object code by offering access from a designated place (gratis or"
                        " for a charge), and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge. You need not require recipients to copy the Corresponding Source along with the object code. If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party) that supports equivalent copying facilities, provided you maintain clear directions next to the object code saying where to find the Corresponding Source. Regardless of what server hosts the Corresponding Source, you remain obligated to ensure that it is available for as long as needed to satisfy these requirements. </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e) Convey the object code using peer-to-peer transmission, provided you inform other peers where the object code and Corresponding Source of the work"
                        " are being offered to the general public at no charge under subsection 6d. </li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">A separable portion of the object code, whose source code is excluded from the Corresponding Source as a System Library, need not be included in conveying the object code work. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">A \u201cUser Product\u201d is either (1) a \u201cconsumer product\u201d, which means any tangible personal property which is normally used for personal, family, or household purposes, or (2) anything designed or sold for incorporation into a dwelling. In determining whether a product is a consumer product, doubtful cases shall be resolved in favor of coverage. For a particular "
                        "product received by a particular user, \u201cnormally used\u201d refers to a typical or common use of that class of product, regardless of the status of the particular user or of the way in which the particular user actually uses, or expects or is expected to use, the product. A product is a consumer product regardless of whether the product has substantial commercial, industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">\u201cInstallation Information\u201d for a User Product means any methods, procedures, authorization keys, or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source. The information must suffice to ensure that the continued functioning of the "
                        "modified object code is in no case prevented or interfered with solely because modification has been made. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">If you convey an object code work under this section in, or with, or specifically for use in, a User Product, and the conveying occurs as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient in perpetuity or for a fixed term (regardless of how the transaction is characterized), the Corresponding Source conveyed under this section must be accompanied by the Installation Information. But this requirement does not apply if neither you nor any third party retains the ability to install modified object code on the User Product (for example, the work has been installed in ROM). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px"
                        "; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The requirement to provide Installation Information does not include a requirement to continue to provide support service, warranty, or updates for a work that has been modified or installed by the recipient, or for the User Product in which it has been modified or installed. Access to a network may be denied when the modification itself materially and adversely affects the operation of the network or violates the rules and protocols for communication across the network. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Corresponding Source conveyed, and Installation Information provided, in accord with this section must be in a format that is publicly documented (and with an implementation available to the public in source code form), and must requir"
                        "e no special password or key for unpacking, reading or copying. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section7\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">7</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">. Additional Terms. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">\u201cAdditional permissions\u201d are terms that supplement the terms of this License by making exceptions from one or more of its conditions. Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License, to the extent that they are valid under applicable law. If additional permissions apply only to part of the Program, that part may be used separately"
                        " under those permissions, but the entire Program remains governed by this License without regard to the additional permissions. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">When you convey a copy of a covered work, you may at your option remove any additional permissions from that copy, or from any part of it. (Additional permissions may be written to require their own removal in certain cases when you modify the work.) You may place additional permissions on material, added by you to a covered work, for which you have or can give appropriate copyright permission. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Notwithstanding any other provision of this License, for material you add to a covered work, you may (if "
                        "authorized by the copyright holders of that material) supplement the terms of this License with terms: </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this License; or </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\">c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">d) Limiting the use for publicity purposes of names of licensors or authors of the material; or </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or </li>\n"
"<li style=\" font-family:'Noto Sans'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">f) Requiring indemnification of l"
                        "icensors and authors of that material by anyone who conveys the material (or modified versions of it) with contractual assumptions of liability to the recipient, for any liability that these contractual assumptions directly impose on those licensors and authors. </li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">All other non-permissive additional terms are considered \u201cfurther restrictions\u201d within the meaning of section 10. If the Program as you received it, or any part of it, contains a notice stating that it is governed by this License along with a term that is a further restriction, you may remove that term. If a license document contains a further restriction but permits relicensing or conveying under this License, you may add to a covered work material governed by the terms of that license document, provided that the further restriction does not survive"
                        " such relicensing or conveying. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">If you add terms to a covered work in accord with this section, you must place, in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Additional terms, permissive or non-permissive, may be stated in the form of a separately written license, or stated as exceptions; the above requirements apply either way. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section8\"></a><span style=\" font-family:'No"
                        "to Sans'; font-size:10pt; font-weight:700;\">8</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">. Termination. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">You may not propagate or modify a covered work except as expressly provided under this License. Any attempt otherwise to propagate or modify it is void, and will automatically terminate your rights under this License (including any patent licenses granted under the third paragraph of section 11). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally, unless and until the copyright holder explicitly a"
                        "nd finally terminates your license, and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means, this is the first time you have received notice of violation of this License (for any work) from that copyright holder, and you cure the violation prior to 30 days after your receipt of the notice. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Termination of your rights under this section does not terminate the licenses of parties"
                        " who have received copies or rights from you under this License. If your rights have been terminated and not permanently reinstated, you do not qualify to receive new licenses for the same material under section 10. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section9\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">9</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">. Acceptance Not Required for Having Copies. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">You are not required to accept this License in order to receive or run a copy of the Program. Ancillary propagation of a covered work occurring solely as a consequence of using peer-to-peer transmission to receive a copy likewise does not requi"
                        "re acceptance. However, nothing other than this License grants you permission to propagate or modify any covered work. These actions infringe copyright if you do not accept this License. Therefore, by modifying or propagating a covered work, you indicate your acceptance of this License to do so. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section10\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">1</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">0. Automatic Licensing of Downstream Recipients. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Each time you convey a covered work, the recipient automatically receives a license from the original licensors, to run, modify and propagate that work, subje"
                        "ct to this License. You are not responsible for enforcing compliance by third parties with this License. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">An \u201centity transaction\u201d is a transaction transferring control of an organization, or substantially all assets of one, or subdividing an organization, or merging organizations. If propagation of a covered work results from an entity transaction, each party to that transaction who receives a copy of the work also receives whatever licenses to the work the party's predecessor in interest had or could give under the previous paragraph, plus a right to possession of the Corresponding Source of the work from the predecessor in interest, if the predecessor has it or can get it with reasonable efforts. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License. For example, you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License, and you may not initiate litigation (including a cross-claim or counterclaim in a lawsuit) alleging that any patent claim is infringed by making, using, selling, offering for sale, or importing the Program or any portion of it. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section11\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">1</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">1. Patents. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-family:'Noto Sans'; font-size:10pt;\">A \u201ccontributor\u201d is a copyright holder who authorizes use under this License of the Program or a work on which the Program is based. The work thus licensed is called the contributor's \u201ccontributor version\u201d. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">A contributor's \u201cessential patent claims\u201d are all patent claims owned or controlled by the contributor, whether already acquired or hereafter acquired, that would be infringed by some manner, permitted by this License, of making, using, or selling its contributor version, but do not include claims that would be infringed only as a consequence of further modification of the contributor version. For purposes of this definition, \u201ccontrol\u201d includes the right to grant patent sublicenses in a manner consistent with the requ"
                        "irements of this License. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Each contributor grants you a non-exclusive, worldwide, royalty-free patent license under the contributor's essential patent claims, to make, use, sell, offer for sale, import and otherwise run, modify and propagate the contents of its contributor version. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">In the following three paragraphs, a \u201cpatent license\u201d is any express agreement or commitment, however denominated, not to enforce a patent (such as an express permission to practice a patent or covenant not to sue for patent infringement). To \u201cgrant\u201d such a patent license to a party means to make such an agreement or commitmen"
                        "t not to enforce a patent against the party. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">If you convey a covered work, knowingly relying on a patent license, and the Corresponding Source of the work is not available for anyone to copy, free of charge and under the terms of this License, through a publicly available network server or other readily accessible means, then you must either (1) cause the Corresponding Source to be so available, or (2) arrange to deprive yourself of the benefit of the patent license for this particular work, or (3) arrange, in a manner consistent with the requirements of this License, to extend the patent license to downstream recipients. \u201cKnowingly relying\u201d means you have actual knowledge that, but for the patent license, your conveying the covered work in a country, or your recipient's use of the covered work in a country"
                        ", would infringe one or more identifiable patents in that country that you have reason to believe are valid. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">If, pursuant to or in connection with a single transaction or arrangement, you convey, or propagate by procuring conveyance of, a covered work, and grant a patent license to some of the parties receiving the covered work authorizing them to use, propagate, modify or convey a specific copy of the covered work, then the patent license you grant is automatically extended to all recipients of the covered work and works based on it. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">A patent license is \u201cdiscriminatory\u201d if it does not include within the scope of "
                        "its coverage, prohibits the exercise of, or is conditioned on the non-exercise of one or more of the rights that are specifically granted under this License. You may not convey a covered work if you are a party to an arrangement with a third party that is in the business of distributing software, under which you make payment to the third party based on the extent of your activity of conveying the work, and under which the third party grants, to any of the parties who would receive the covered work from you, a discriminatory patent license (a) in connection with copies of the covered work conveyed by you (or copies made from those copies), or (b) primarily for and in connection with specific products or compilations that contain the covered work, unless you entered into that arrangement, or that patent license was granted, prior to 28 March 2007. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'"
                        "Noto Sans'; font-size:10pt;\">Nothing in this License shall be construed as excluding or limiting any implied license or other defenses to infringement that may otherwise be available to you under applicable patent law. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section12\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">1</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">2. No Surrender of Others' Freedom. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">If conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot convey a covered work so as to satisfy simul"
                        "taneously your obligations under this License and any other pertinent obligations, then as a consequence you may not convey it at all. For example, if you agree to terms that obligate you to collect a royalty for further conveying from those to whom you convey the Program, the only way you could satisfy both those terms and this License would be to refrain entirely from conveying the Program. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section13\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">1</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">3. Use with the GNU Affero General Public License. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Notwithstanding any other provision of this License, you "
                        "have permission to link or combine any covered work with a work licensed under version 3 of the GNU Affero General Public License into a single combined work, and to convey the resulting work. The terms of this License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section14\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">1</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">4. Revised Versions of this License. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The Free Software Found"
                        "ation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License \u201cor any later version\u201d applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section15\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">1</span><span style=\" font-"
                        "family:'Noto Sans'; font-size:10pt; font-weight:700;\">5. Disclaimer of Warranty. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM \u201cAS IS\u201d WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section16\"></a><span style=\" font-fami"
                        "ly:'Noto Sans'; font-size:10pt; font-weight:700;\">1</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">6. Limitation of Liability. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. </span></p>\n"
"<h5 style=\" margin-top:12px; margin-bottom:4p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section17\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">1</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">7. Interpretation of Sections 15 and 16. </span></h5>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">If the disclaimer of warranty and limitation of liability provided above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span st"
                        "yle=\" font-family:'Noto Sans'; font-size:10pt;\">END OF TERMS AND CONDITIONS </span></p>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"howto\"></a><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">H</span><span style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:700;\">ow to Apply These Terms to Your New Programs </span></h4>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'No"
                        "to Sans'; font-size:10pt;\">To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the \u201ccopyright\u201d line and a pointer to where the full notice is found. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    &lt;one line to give the program's name and a brief idea of what it does.&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto"
                        " Sans Mono'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    This program is free software: you can redistribute it and/or modify</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    it under the terms of the GNU General Public License as published by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    the Free Software Foundation, either version 3 of the License, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; "
                        "font-size:10pt;\">    (at your option) any later version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans Mono'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    This program is distributed in the hope that it will be useful,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    but WITHOUT ANY WARRANTY; without even the implied warranty of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    MERCHANTABILITY or FITNE"
                        "SS FOR A PARTICULAR PURPOSE.  See the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    GNU General Public License for more details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans Mono'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    You should have received a copy of the GNU General Public License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    along with this program.  If not, see &lt;https://www.gnu.o"
                        "rg/licenses/&gt;. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">Also add information on how to contact you by electronic and paper mail. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    &lt;program&gt;  Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span styl"
                        "e=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    This is free software, and you are welcome to redistribute it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans Mono'; font-size:10pt;\">    under certain conditions; type `show c' for details. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The hypothetical commands `show w' and `show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a "
                        "GUI interface, you would use an \u201cabout box\u201d. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">You should also get your employer (if you work as a programmer) or school, if any, to sign a \u201ccopyright disclaimer\u201d for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see &lt;</span><a href=\"https://www.gnu.org/licenses/\"><span style=\" font-family:'Noto Sans'; font-size:10pt; text-decoration: underline; color:#00d3b8;\">https://www.gnu.org/licenses/</span></a><span style=\" font-family:'Noto Sans'; font-size:10pt;\">&gt;. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans'; font-size:10pt;\">The GNU General Public License does not permit incorporating your program into proprie"
                        "tary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with the library. If this is what you want to do, use the GNU Lesser General Public License instead of this License. But first, please read &lt;</span><a href=\"https://www.gnu.org/licenses/why-not-lgpl.html\"><span style=\" font-family:'Noto Sans'; font-size:10pt; text-decoration: underline; color:#00d3b8;\">https://www.gnu.org/licenses/why-not-lgpl.html</span></a><span style=\" font-family:'Noto Sans'; font-size:10pt;\">&gt;. </span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.licenseTab), QCoreApplication.translate("AboutDialog", u"License", None))
        self.copyrightLabel.setText(QCoreApplication.translate("AboutDialog", u"Copyright \u00a9 2024 Marko Peji\u0107", None))
        self.closeDialogButton.setText(QCoreApplication.translate("AboutDialog", u"Close", None))
    # retranslateUi

