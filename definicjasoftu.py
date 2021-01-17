def ping(address, count=1):
	cmd = ['ping']
	if sys.platform in ('windows', 'win32'):
		cmd.append('-n')
	print("Platforma: Windows")	
 
	elif sys.platform.startswith('linux'):
		cmd.append('-c')
	print("Platforma: Linux")
 
	elif sys.platform.startswith('freebsd'):
		cmd.append('-c')
	print("Platforma: FreeBSD")
 
	else sys.platform.startswitch('darwin'):
		cmd.append('-c')
	print("Platforma: MacosX")
    