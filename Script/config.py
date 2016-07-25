[Server]
Platforms = b2b2b
SoftName = Tomcat
ItemRoot = /opt
WarPath = /Package/War
ItemList = Service|Mail|Solr|Front|Background|WeChat|Mobile
BackupPath = /opt/Backup
ConfigPath = /Package/War/Configure
ItemConfigPath = /WEB-INF/classes/properties
ProjectHome = /opt/Project

[Service]
ServiceWar = b2b2b-service.war
War = b2b2b-service.war

[Mail]
MailWar = b2b2b-mail-service.war
War = b2b2b-mail-service.war

[Solr]
SolrWar = b2b2b-solr-service.war
War = b2b2b-solr-service.war

[Front]
FrontWar = b2b2b-front.war
War = b2b2b-front.war

[Background]
BackgroundWar = b2b2b-back.war
War = b2b2b-back.war

[WeChat]
WeChatWar = b2b2b-WX.war
War = b2b2b-WX.war

[Mobile]
MobileWar = b2b2b-mobile.war
War = b2b2b-mobile.war