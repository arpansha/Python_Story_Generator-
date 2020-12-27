import random

def story_genrator(your_name,partner_name,story_language,story):
	if story_language == 'English':
		main_story = (story.replace('Smith',your_name)).replace('David',partner_name)
	else:
		main_story = ((story.replace('smith',your_name)).replace('devid',partner_name))
	return main_story


your_name = input("Please Enter Your Name:-")
partner_name = input("Please Enter Your Partner Name:-")
story_type = input("Enter Your Story Type Like Motivation,Love,Comedy:-")
story_language = input("Enter Your Story Language:-")

if story_language == 'English':
	if story_type == 'Motivation':
		story = ''' Once upon a time there were two kids one six years old Smith and twelve years old David. They were so close since childhood. One day while playing they came far away from the village. And it so that happened  the 12 years old David felt in well near by there. 
And 6 years old Smith started screaming for help but there were no one even at far distance. Small child Smith saw a bucket and rope tide to it. He didn't wasted a second, he threw that bucket in to the well and asked to David to hold it. 
Then he started pulling a rope and he went on pulling until he saved his elder friend David. Then they hugged each other happily and went back to village.When they told this incident to the village people, they surprised since it was hard to believe. 
A kid (Smith) who don't have enough strength to lift a full water bucket, how could he dragged a boy (David) who was elder than him by 6 years.The village people went to old man who was well known in the village and was the most wise person. 
They told him the whole story and asked, "How is it possible that a kid (Smith) who don't have enough strength to lift a water bucket how could he dragged a boy (David) who was elder than him by 6 years?"
When a old man listened the story he said that "What can I tell you about this, the kid (Smith) do said things very clearly". "What more I can tell you?" See  the question is not how could he saved him, it is why could he saved him. It is only the answer, when he did that there were no one even at far distance to tell him that you can't do this. 
'''
		print(story_genrator(your_name,partner_name,story_language,story))

	elif story_type == 'Love':
		story = []
	elif story_type == 'Comedy':
		story = []
	else:
		print("Please Write Correct Story Type")
elif story_language == 'Hindi':
	if story_type == 'Motivation':

		story = ''' ek baar do bachche the ek chhah saal ka smith aur baarah saal ka devid. ve bachapan se itane kareeb the. ek din khelate samay ve gaanv se bahut door aa gae. aur aisa hua ki 12 saal ke devid ko vahaan ke paas mein achchhee tarah se mahasoos hua.
aur 6 saal ka smith madad ke lie chillaane laga lekin door-door tak bhee koee nahin tha. chhote bachche smith ne ek baaltee aur rassee ko dekha. usane ek sekand bhee barbaad nahin kiya, usane us baaltee ko kune mein phenk diya aur devid se kaha ki ise pakado.
phir usane ek rassee kheenchana shuroo kiya aur vah tab tak kheenchata raha jab tak ki usane apane bade dost devid ko nahin bacha liya. tab ve ek-doosare ko khushee-khushee gale lagaate the aur gaanv vaapas chale jaate the. jab unhonne gaanv ke logon ko yah ghatana bataee, to ve aashcharyachakit rah gae kyonki yah vishvaas karana kathin tha.
ek bachcha (smith) jisake paas pooree paanee kee baaltee uthaane ke lie paryaapt taakat nahin hai, vah 6 saal tak ek ladake (devid) ko kis tarah se ghaseet sakata tha. gaanv ke log boodhe aadamee ke paas jaate the jo achchhee tarah se jaana jaata tha gaanv aur sabase buddhimaan vyakti tha.
unhonne use pooree kahaanee sunaee aur poochha, "yah kaise sambhav hai ki ek bachcha (smith) jo paanee kee baaltee uthaane ke lie paryaapt taakat nahin rakhata hai, vah 6 saal tak ek ladake (devid) ko kaise kheench sakata hai jo usase bada tha?" "
jab ek boodhe vyakti ne kahaanee sunee to usane kaha ki "main aapako is baare mein kya bata sakata hoon, bachcha (smith) ne bahut spasht roop se kaha hai". "main aapako aur kya bata sakata hoon?" dekhie savaal yah nahin hai ki vah use kaise bacha sakata tha, yahee vajah hai ki vah use bacha sakata tha. yah keval uttar hai, jab usane aisa kiya ki use bataane ke lie door-door tak bhee koee nahin tha ki aap aisa nahin kar sakate. '''
		print(story_genrator(your_name,partner_name,story_language,story))

	elif story_type == 'Love':
		story = []
	elif story_type == 'Comedy':
		story = []
	else:
		print("Undifine Story Type")
else:
	print("We Are Provide Only Two Languages Hindi or English:-")













