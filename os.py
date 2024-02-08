import easygui
import platform,socket,re,uuid,psutil

system = platform.system()
release = platform.release()
verison = platform.version()
machine = platform.machine()
hostname = socket.gethostname(),
ip_address = socket.gethostbyname(socket.gethostname())
mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
cpu = platform.processor()
ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"


easygui.msgbox(f'This Is Your PC Informations:\n >system: {system}\n >release: {release}\n >verison: {verison}\n >machine: {machine}\n >pc name: {hostname}\n >ip address: {ip_address}\n >mac address: {mac_address}\n >cpu: {cpu}\n >ram: {ram}', 'PC INFORMATIONS')