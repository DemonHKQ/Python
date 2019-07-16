适用于python3
新增了对404域名的过滤 ，用Excel代替了txt，增加对子域端口的扫描（可自行增添对应端口）

tcp 20,21    FTP（文件传输协议）    允许匿名的上传下载,爆破,嗅探,win提权,远程执行(proftpd 1.3.5),各类后门(proftpd,vsftp 2.3.4)
tcp 22    SSH （安全外壳协议 ）    可根据已搜集到的信息尝试爆破,v1版本可中间人,ssh隧道及内网代理转发,文件传输等等
tcp 23    Telnet （ 远程终端协议）    爆破,嗅探,一般常用于路由,交换登陆,可尝试弱口令
tcp 25    SMTP（简单邮件传输协议）    邮件伪造,vrfy/expn查询邮件用户信息,可使用smtp-user-enum工具来自动跑
tcp/udp 53    DNS（域名系统）    允许区域传送,dns劫持,缓存投毒,欺骗以及各种基于dns隧道的远控
tcp/udp 69    TFTP （简单文件传送协议 ）    尝试下载目标及其的各类重要配置文件
tcp 80-89,443,8440-8450,8080-8089    各种常用的Web服务端口    可尝试经典的topn,vpn,owa,webmail,目标oa,各类Java控制台,各类服务器Web管理面板,各类Web中间件漏洞利用,各类Web框架漏洞利用等等……
tcp 110    POP3（邮局协议版本3 ）    可尝试爆破,嗅探
tcp 111,2049    NFS（网络文件系统）    权限配置不当
tcp 137,139,445    SMB（NETBIOS协议）    可尝试爆破以及smb自身的各种远程执行类漏洞利用,如,ms08-067,ms17-010,嗅探等……
tcp 143    IMAP（邮件访问协议）    可尝试爆破
udp 161    SNMP（简单网络管理协议）    爆破默认团队字符串,搜集目标内网信息
tcp 389    LDAP（ 轻量目录访问协议 ）    ldap注入,允许匿名访问,弱口令
tcp 512,513,514    Linux rexec （远程登录）    可爆破,rlogin登陆
tcp 873    Rsync （数据镜像备份工具）    匿名访问,文件上传
tcp 1194    OpenVPN（虚拟专用通道）    想办法钓VPN账号,进内网
tcp 1352    Lotus（Lotus软件）    弱口令,信息泄漏,爆破
tcp 1433    SQL Server（数据库管理系统）    注入,提权,sa弱口令,爆破
tcp 1521    Oracle（甲骨文数据库）    tns爆破,注入,弹shell…
tcp 1500    ISPmanager（ 主机控制面板）    弱口令
tcp 1723    PPTP（点对点隧道协议 ）    爆破,想办法钓VPN账号,进内网
tcp 2082,2083    cPanel （虚拟机控制系统 ）    弱口令
tcp 2181    ZooKeeper（分布式系统的可靠协调系统 ）    未授权访问
tcp 2601,2604    Zebra （zebra路由）    默认密码zerbra
tcp 3128    Squid （代理缓存服务器）    弱口令
tcp 3312,3311    kangle（web服务器）    弱口令
tcp 3306    MySQL（数据库）    注入,提权,爆破
tcp 3389    Windows rdp（桌面协议）    shift后门[需要03以下的系统],爆破,ms12-020
tcp 3690    SVN（开放源代码的版本控制系统）    svn泄露,未授权访问
tcp 4848    GlassFish（应用服务器）    弱口令
tcp 5000    Sybase/DB2（数据库）    爆破,注入
tcp 5432    PostgreSQL（数据库）    爆破,注入,弱口令
tcp 5900,5901,5902    VNC（虚拟网络控制台，远控）    弱口令爆破
tcp 5984    CouchDB（数据库）    未授权导致的任意指令执行
tcp 6379    Redis（数据库）    可尝试未授权访问,弱口令爆破
tcp 7001,7002    WebLogic（WEB应用系统）    Java反序列化,弱口令
tcp 7778    Kloxo（虚拟主机管理系统）    主机面板登录
tcp 8000    Ajenti（Linux服务器管理面板）    弱口令
tcp 8443    Plesk（虚拟主机管理面板）    弱口令
tcp 8069    Zabbix （系统网络监视）    远程执行,SQL注入
tcp 8080-8089    Jenkins,JBoss （应用服务器）    反序列化,控制台弱口令
tcp 9080-9081,9090    WebSphere（应用服务器）    Java反序列化/弱口令
tcp 9200,9300    ElasticSearch （Lucene的搜索服务器）    远程执行
tcp 11211    Memcached（缓存系统）    未授权访问
tcp 27017,27018    MongoDB（数据库）    爆破,未授权访问
tcp 50070,50030    Hadoop（分布式文件系统）    默认端口未授权访问