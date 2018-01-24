from threading import Timer
import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
import glob
import re
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()


#define function that checks for mouse location
def main_click():
	click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
	#now check to see if previous  was pressed
        if 10 <= click_pos[0] <= 60 and 180 <= click_pos[1] <=230:
                print "You pressed button previous"
                button(4)

	 #now check to see if next  was pressed
        if 70 <= click_pos[0] <= 120 and 180 <= click_pos[1] <=230:
                print "You pressed button next"
                button(5)

	 #now check to see if button 9 was pressed
        if 15 <= click_pos[0] <= 125 and 165 <= click_pos[1] <=200:
                print "You pressed button 9"
                button(9)
	if 0 <= click_pos[0] <= 320 and 20 <= click_pos[1] <= 130:
		print "You clicked screen"
		button(10)

	if 280 <= click_pos[0] <= 320 and 0 <= click_pos[1] <= 40:
		print "You click blank"
		button(11)
	
	if 140 <= click_pos[0] <= 310 and 180 <= click_pos[1] <= 230:
		print "Show networks"
		button(12)

def network_click():
	click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
	print "you selected a network"
	if 40 <= click_pos[0] <= 320 and 40 <= click_pos[1] <= 100:
		station_list(BBC_START)
		station_screen(1)
	if 40 <= click_pos[0] <= 320 and 105 <= click_pos[1] <= 165:
		station_list(DI_START)
		station_screen(2)
	if 40 <= click_pos[0] <= 320 and 170 <= click_pos[1] <= 230:
		station_list(SOMA_START)
		station_screen(3)

def station_click():
	click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
	if 40 <= click_pos[0] <= 125 and 40 <= click_pos[1] <= 73:
		station(0)
	if 131 <= click_pos[0] <= 218 and 40 <= click_pos[1] <= 73:
		station(1)
	if 222 <= click_pos[0] <= 307 and 40 <= click_pos[1] <= 73:
		station(2)
	if 40 <= click_pos[0] <= 125 and 79 <= click_pos[1] <= 112:
		station(3)
	if 131 <= click_pos[0] <= 218 and 79 <= click_pos[1] <= 112:
		station(4)
	if 222 <= click_pos[0] <= 307 and 79 <= click_pos[1] <= 112:
		station(5)
	if 40 <= click_pos[0] <= 125 and 118 <= click_pos[1] <= 151:
		station(6)
	if 131 <= click_pos[0] <= 218 and 118 <= click_pos[1] <= 151:
		station(7)
	if 222 <= click_pos[0] <= 307 and 118 <= click_pos[1] <= 151:
		station(8)
	if 40 <= click_pos[0] <= 125 and 157 <= click_pos[1] <= 190:
		station(9)
	if 131 <= click_pos[0] <= 218 and 157 <= click_pos[1] <= 190:
		station(10)
	if 222 <= click_pos[0] <= 307 and 157 <= click_pos[1] <= 190:
		station(11)
	if 40 <= click_pos[0] <= 125 and 196 <= click_pos[1] <= 229:
		station(12)
	if 131 <= click_pos[0] <= 218 and 196 <= click_pos[1] <= 229:
		station(13)
	if 222 <= click_pos[0] <= 307 and 196 <= click_pos[1] <= 229:
		station(14)
	if 0 <= click_pos[0] <= 40 and 0 <= click_pos[1] <= 120:
		station_list(shown_stations[0]-15)
		if shown_stations[14] < SOMA_START:
			station_screen(2)
		else:
			station_screen(3)
	if 0 <= click_pos[0] <= 40 and 120 <= click_pos[1] <= 240:
		station_list(shown_stations[14])
		if shown_stations[14] < SOMA_START:
			station_screen(2)
		else:
			station_screen(3)

#define action on pressing buttons
def button(number):
	print "You pressed button ",number
	if number == 0:    #specific script when exiting
		screen.fill(black)
		font=pygame.font.Font(None,24)
        	label=font.render("Radioplayer will continue in background", 1, (white))
        	screen.blit(label,(0,90))
		pygame.display.flip()
		time.sleep(5)
		sys.exit()

	if number == 1:	
		subprocess.call("mpc play ", shell=True)
		refresh_menu_screen()

	if number == 2:
		subprocess.call("mpc stop ", shell=True)
		refresh_menu_screen()

	if number == 3:
		subprocess.call("mpc stop ", shell=True)
		refresh_menu_screen() 
		
	if number == 4:
		subprocess.call("mpc prev ", shell=True)
		refresh_menu_screen()

	if number == 5:
		subprocess.call("mpc next ", shell=True)
		refresh_menu_screen()

	if number == 6:
		subprocess.call("mpc volume -10 ", shell=True)
		refresh_menu_screen()

	if number == 7:
		subprocess.call("mpc volume +10 ", shell=True)
		refresh_menu_screen()

	if number == 8:
		subprocess.call("mpc volume 0 ", shell=True)
		refresh_menu_screen()
	if number == 10:
		refresh_menu_screen()	
	if number == 11:
		blank_screen()
	if number == 12:
		network_screen()

def station(box):
	station_num = shown_stations[box]
	subprocess.call("mpc play "+str(station_num+1), shell=True)
	refresh_menu_screen()

def blank_screen():
	screen.fill(black)
	pygame.display.flip()

def refresh_menu_screen():
	global view
	view = MAIN
#set up the fixed items on the menu
	screen.fill(black) #change the colours if needed
	# draw the main elements on the screen
#	screen.blit(play,(20,80))	
#	screen.blit(pause,(80,80))
#	screen.blit(refresh,(270,70))
	screen.blit(previous,(10,180))
	screen.blit(next,(70,180))
#       screen.blit(vol_down,(130,180))
#	screen.blit(vol_up,(190,180))
#	screen.blit(mute,(250,180))	
#       screen.blit(exit,(270,5))
#	screen.blit(radio,(2,1))

	pygame.draw.rect(screen, gray, (140,180,170,50))
	list_button = font.render('station list', 1, (black))
	screen.blit(list_button,(180,195))

	##### display the station name and split it into 2 parts : 
	station = subprocess.check_output("mpc current", shell=True )
	lines=station.split(":")

	if 'SomaFM' in station:
		lines = station.split("[SomaFM]:")
		st_line = lines[0]
		st_line1 = 'somaFM'
		st_line2 = lines[0].replace("from SomaFM.com","")
		st_line2 = st_line2.replace("SomaFM","")
		st_line2 = st_line2.replace("[]","") 
	elif 'Digitally Imported' in station:
		st_line = lines[0].split(" - ",1)
		st_line1 = 'Digitally Imported'
		st_line2 = st_line[0]
	elif 'bbc_' in station:
		st_line1 = 'BBC Radio'
		if 'radio_one' in station:
			st_line1 = 'BBC Radio 1'
		elif '1xtra' in station:
			st_line1 = 'BBC Radio 1xtra'
		elif 'radio_two' in station:
			st_line1 = 'BBC Radio 2'
		elif 'radio_three' in station:
			st_line1 = 'BBC Radio 3'
		elif 'radio_fourfm' in station:
			st_line1 = 'BBC Radio 4'
		elif 'radio_four_extra' in station:
			st_line1 = 'BBC Radio 4 Extra'
		elif '6music' in station:
			st_line1 = 'BBC Radio 6'
		st_line2 = ''
	else:
		st_line1 = lines[0][:-1]
		st_line2 = ''
	
	length = len(lines) 
	if length==1:
		line1 = lines[0]
		line1 = line1[:-1]
		line2 = "No additional info: "
	else:
		line1 = lines[0]
		line2 = lines[1]

	line2 = line2.replace('[SomaFM]','')
	lineN = line2.split(' - ',1)
	lineN[0] = lineN[0].replace("SomaFM's ","")
	if len(lineN)>1:
		lineN[1] = lineN[1][:-1]
		song = lineN[1].split('(',1)
		lineN[1] = song[0]

		if len(song)>1:
			lineN.append('('+song[1])
		else:
			lineN.append('')
	else:
		lineN.append('')
		lineN.append('')


	#trap no station data
	if line1 =="":
		line2 = "Press PLAY or REFRESH"
		station_status = "stopped"
		status_font = red
	else:
		station_status = "playing"
		status_font = green
	network_name=station_font.render(st_line1, 1, (red))
	station_name=station_font.render(st_line2, 1, (red))
	additional_data1=title_font.render(lineN[0], 1, (blue))
	additional_data2=title_font.render(' - '+lineN[1], 1, (blue))
	additional_data3=title_font.render('    '+lineN[2], 1, (blue))
#	station_label=font.render(station_status, 1, (status_font))
#	screen.blit(station_label,(2,1))
	screen.blit(network_name,(25,20))
	screen.blit(station_name,(5,50))
	screen.blit(additional_data1,(12,80))
	screen.blit(additional_data2,(12,110))
	screen.blit(additional_data3,(12,140))
	######## add volume number
#	volume = subprocess.check_output("mpc volume", shell=True )
#	volume = volume[8:]
#	volume = volume[:-1]
#	volume_tag=font.render(volume, 1, (black))
#	screen.blit(volume_tag,(175,75))
	####### check to see if the Radio is connected to the internet
	IP = subprocess.check_output("hostname -I", shell=True )
	IP=IP[:3]
	if IP =="192":
		network_status = "online"
		status_font = gray

	else:
		network_status = "offline"
		status_font = red

	network_status_label = font.render(network_status, 1, (status_font))
	screen.blit(network_status_label, (2,1))
	pygame.display.flip()

#display station (in network) view
def station_screen(network):
	global view
	view = STATION
	screen.fill(black)
	if network == 1:
		heading = title_font.render("BBC", 1, (red))
		screen.blit(heading,(40,5))
	elif network == 2:
		heading = title_font.render("Digitally Imported", 1, (red))
		screen.blit(heading,(40,5))
	else:
		heading = title_font.render("somaFM", 1, (red))
		screen.blit(heading,(40,5))
	next_button = station_font.render('<', 1, (gray))
	screen.blit(next_button,(10,60))
	exit_button = station_font.render('>', 1, (gray))
	screen.blit(exit_button,(10,160))
	
	i = 0
	x = 40
	y = 40
	while y <= 196:
		while x <= 222:
			pygame.draw.rect(screen, white, (x,y,85,33), 1)
			st_name = all_stations[shown_stations[i]]
			st_label = clean_station(st_name)
			screen.blit(st_label,(x+3,y+10))
			i += 1
			x += 91
		y += 39
		x = 40
	pygame.display.flip()

#truncate station based on length
def clean_station(station):
	while 1:
		size = small_font.size(station)
		if size[0] > 83:
			station = station[:-1]
		else:
			break
	return small_font.render(station, 1, (white))

#display network view
def network_screen():
	global view
	view = NETWORK
	screen.fill(black)
	pygame.draw.rect(screen, white, (40,40,281,60), 1)
	pygame.draw.rect(screen, white, (40,105,281,60), 1)
	pygame.draw.rect(screen, white, (40,170,281,60), 1)

	network1 = station_font.render('BBC Radio', 1, (white))
	network2 = station_font.render('Digitally Imported', 1, (white))
	network3 = station_font.render('somaFM', 1, (white))

	screen.blit(network1, (50,55))
	screen.blit(network2, (50,120))
	screen.blit(network3, (50,185))

	pygame.display.flip()

def station_list(start):
	global shown_stations
	i = 0
	while i < 15:
		if start == STATION_COUNT:
			start = 0
		shown_stations[i] = start
		i += 1
		start += 1

def timeout():
	subprocess.call("mpc stop", shell=True)
	blank_screen()
	print "Timeout"

def main():
#	for x in tracks:
#		t += 1
#		print t

#	t = Timer(30.0, timeout).start()
        while 1:
                for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
#				t.cancel()
                                print "screen pressed" #for debugging purposes
                                pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                print pos #for checking
                                pygame.draw.circle(screen, white, pos, 2, 0) #for debugging purposes - adds a small dot where the screen is pressed
				if view == MAIN:
	                                main_click()
				elif view == NETWORK:
					network_click()
				elif view == STATION:
					station_click()

#ensure there is always a safe way to end the program if the touch screen fails

                        if event.type == KEYDOWN:
#				t.cancel()
                                if event.key == K_ESCAPE:
                                        sys.exit()
#		t = Timer(30.0, timeout).start()
	pygame.display.update()


#################### EVERTHING HAS NOW BEEN DEFINED ###########################

subprocess.call("mpc volume 100", shell=True)

#set size of the screen
size = width, height = 320, 240
screen = pygame.display.set_mode(size)

#print subprocess.call("mpc playlist", shell=True)

small_font=pygame.font.Font(None,14)
font=pygame.font.Font(None,24)
title_font=pygame.font.Font(None,35)
station_font=pygame.font.Font(None,45)

#play=pygame.image.load("play.tiff")
#pause=pygame.image.load("pause.tiff")
#refresh=pygame.image.load("refresh.tiff")
previous=pygame.image.load("previous.tiff")
next=pygame.image.load("next.tiff")
#vol_down=pygame.image.load("volume_down.tiff")
#vol_up=pygame.image.load("volume_up.tiff")
#mute=pygame.image.load("mute.png")
#exit=pygame.image.load("exit.tiff")
#radio=pygame.image.load("radio.tiff")

MAIN = 1
NETWORK = 2
STATION = 3
view = MAIN

BBC_START = 0
DI_START = 5
SOMA_START = 96
STATION_COUNT = 124
all_stations = open('stations.txt', 'r').read().split('\n')
shown_stations = [0]*15

#define colours
blue = 26, 0, 255
cream = 254, 255, 25
black = 0, 0, 0
white = 255, 255, 255
gray = 50,50,50
yellow = 255, 255, 0
red = 255, 0, 0
green = 0, 255, 0
refresh_menu_screen()  #refresh the menu interface 
main() #check for key presses and start emergency exit
station_name()

