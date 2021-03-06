#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:03:49 2020

@author: n_rishabh
"""


from chatterbot import ChatBot
chatbot = ChatBot("Ron")

from chatterbot.trainers import ListTrainer

from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ListTrainer(chatbot)

trainer.train([
    "I m not able to access my Bitrix24 account?",
    "Go to https://cloudcounselage24.bitrix24.com/ On the Login page, In the, ‘Enter the phone number or email’, type in your email id that you have registered with Cloud Counselage and Click ‘Forgot Password’. In case the problem persists, please write a mail to hrsupport@cloudcounselage.in",
])

trainer.train([
    "What is the job profile? Will we be able to work only in the tech we have chosen for the internship?",
    "Your job profile is 'Technology - Intern'; if you're in cloud computing technology to update in your LinkedIn or resume, you can write as 'Cloud Computing - Intern'. Yes, you'll only work in the technology you're selected for but you can take the training of other technologies.",
])

trainer.train([
    "How many workgroups will an intern be a part of?/ How many workgroups should I be in?",
    "Every intern should be a part of 2 workgroups. 1. '202003-IP'  -- This is a general workgroup. Everyone who is enrolled in IP should be a part of this workgroup. 2. '202003-IP-Technology'  -- This is a technology-specific workgroup. You'll be added to the technology you had enrolled for. For example '202003-IP-Python' for students who enrolled for python.If anyone has not been added to any of these workgroups, kindly message 'Cloud Counselage HR' regarding the same over bitrix24 platform.",
])

trainer.train([
    "Not able to access the LP1 page with my token/ When I put my token it redirects me to the home page/ Getting error while accessing the page- 'User Not Found'/Website Redirection Issue/Tokens not working.",
    "Please watch the videos shared with the invite and you should not face any problems in accessing the training. Please follow the protocol shown in the videos.",
])

trainer.train([
    "Login issues with training/ for every module of LP1/ LP2, do we have to register again for access to the content?",
    "Yes, you need to register for every module of training. Some of you are facing login issues, we have kept the training visible without login. Even then, to post a comment and give a quiz you'll have to login. In case you face difficulty to do so, please try to perform your quiz or post a comment by using a different browser or incognito mode.",
])

trainer.train([
    "I am applying my 2nd token that is the LP1 then it shows invalid user but the first token was accepted. What should I do?/ Tokens not working",
    "For each training of LP1, there are different tokens. Please read the tasks or watch the videos again meticulously. Try accessing it in incognito mode.",
])

trainer.train([
    "I did follow the instructions given in the video, but still, I'm not able to log in for the LP1 task",
    "Ensure you're using the right token",
])

trainer.train([
    "Do I need to pass with the certificate in training.",
    "No, but please ensure you complete the training.",
])

trainer.train([
    "I am not able to see my tasks.",
    " Please remove the default 'In Progress' from your filter of the task section and try.",
])

trainer.train([
    "What do we do in the work report?",
    "As mentioned in the video, please write what you have done this week and request approval from your supervisor by clicking on 'send to supervisor'.",
])

trainer.train([
    "I tried it 3-4 times and have to enter token each time I visit it.",
    "We understand that it sometimes becomes tedious to access the training and we highly appreciate your support in making the training possible. We only do this for security reasons and we're trying to find a way to minimise the token use. For now, please note that in LP1 there are 3 types tokens: 1) One for each technology, you're a part of. 2) The lp1 home page. 3) The 6 tokens (one for each step)",
])

trainer.train([
    "I just joined the group and I am not understanding what to do further. How do I start my internship?",
    "Please go through the mail from which you have accepted the invite and check the task section as well.",
])

trainer.train([
    "What do I do after completing the quiz? how to complete the entire lp1",
    "There are tokens for each training in the task, if this learning path is done, please wait for the next learning path to begin and then please try to finish it. If you are done with LP3 please wait for Live Projects to begin.",
])

trainer.train([
    "Do I need to register every time I do different tasks of lp1?",
    "There are codes in the LP1 assignment, and each time you have to register also, please check your task description.",
])

trainer.train([
    "I have complete one training, I didn't find any options to continue my training.",
    "Go back to the technology Page. Enter the respective tokens and then work. follow the same process every time.",
])

trainer.train([
    "I am not getting results of the training.",
    "They are just for your practice and not for our record, so you don't need the results of LP1 and LP2 training.",
])

trainer.train([
    "Unable to access the quiz",
    "Please retry after some time in an incognito window",
])

trainer.train([
    "Hi there!",
    "Hello",
])

trainer.train([
    "What to do after completing LP1/ LP2/ LP3?",
    "Mark your task as finished and wait for the next instructions.",
])

trainer.train([
    "Which Browser I should use?",
    "Google Chrome is recommended.",
])

trainer.train([
    "Do we need to complete all the six steps within 14 hours as you mentioned that we have to complete all the 6 steps within 2 weeks so it becomes 14 hours?",
    "It's preferred if you complete the LP1 training in 2 weeks but not mandatory. LP1, LP2, and LP3 are expected to be completed before the live projects start in July; but that doesn't mean you should give anything less than 1 hour a day or 7 hours a week towards the learning paths (LP).",
])

trainer.train([
    "I had press finished button of LP1 task but want to resume the task, how to do that?",
    "You can go back to that task and then click on 'More' and then 'resume' to restart that task.",
])

trainer.train([
    "The web pages on mobile are not showing properly.",
    "They are purposefully only configured for Desktops/ Laptops. In an emergency, you can use the 'show as desktop' mode of your browser.",
])

trainer.train([
    "I have opted for a blockchain internship, can I also learn about AI and do an internship in both? ",
    "You can learn both the technologies using Learning Path 2 (LP2) which will begin after the 2nd week of March, but your internship will only be continuing with the one you are selected for.",
])

trainer.train([
    "Can I switch my technology now? / I had enrolled for two technologies at the time of form-filling and got selected for the technology I’m not interested in.",
    "You cannot switch the technology currently. You have to continue with the one you are selected for. In the case of multiple form entries, you just got selected for one of them; the first one that you entered. You cannot make a switch right now.",
])

trainer.train([
    "Can you help me by telling how can I get to know about my progress of LP 1",
    "There is no metric to score your progress in any learning paths as it will be at a different pace for every individual.",
])

trainer.train([
    "I am not able to view a page/ I am logged in the training and still the website asks me to login",
    "This could be because of some issue in the cookies or extension in your browser. Please try again with a different browser or open the tab with incognito mode. Also, you don't need to record your results, the quizzes are only for your knowledge check and not a metric to score you.",
])

trainer.train([
    "I am having trouble finding the workgroup ( no workgroup is visible)",
    "Please ensure that you have connected to the drive of that workgroup by going to your notification and connecting to the drive of that workgroup. If that is done, please try to search for your workgroup in the search bar at the top of your screen. To search, use the keywords, 202003-IP-TechnologyName. Ex '202003-IP-DevOps'. In case there is no invitation to you, please message Cloud Counselage HR. You will be added to 2 groups '202003-IP' which is a general workgroup and the other one is '202003-IP-Technology' which is a technology-specific workgroup.",
])

trainer.train([
    "I am not added into my technology workgroup./ actually there are n no of tokens and every token I entered it is showing user no found or redirecting to the same page",
    "Please follow the instructions given in the videos or the one in the Bitrix24 mail (these are the same videos share in the task), the tokens are given to you. Ensure that you are putting the right token on the right page.",
])

trainer.train([
    "When does the LP1/ LP2/ LP3 begin dates and deadline/ end date?",
    "The dates to begin the learning paths (LP) are: - LP1 - 01/03/2020 LP2 - 18/03/2020 LP3 - 02/04/2020 All learning Paths (LP) are expected to be completed by the interns before the first   week of June as Live Projects will begin in that time frame. ",
])

trainer.train([
    "What happens in LP2? What kind of training can we expect? Is it a Basic/Advance level?",
    "The main focus of LP2 is to provide you with a basic foundation of the technology you're interested in. The training is also handpicked in such a way that they enable you to work on LP3 assignments which interim gives you the beginning to start your study for the selected technology and in no terms is the only/ final training you should look into. Please keep learning after your LP2 is complete, that is the only way to grow in your technology of choice.",
])

trainer.train([
    "What happens in LP3? What kind of training can we expect? Is it a Basic/Advance level?",
    "LP3 will be assignment based and its execution and content vary from technology to technology. This assignment will be like a mini-project for all interns in a particular technology which will be verified by Cloud Counselage Project Managers.",
])

trainer.train([
    "What to do after LP3?",
    " You'll be given preparatory leave (PL) from April to June after that your Live Projects will be given after the first week of June.",
])

trainer.train([
    "Can we skip any training if we are already clear with the basics?",
    "No, these pieces of training will cover basics and there is no harm in brushing up your skills before you start with the assignments later.",
])

trainer.train([
    "Is it ok to clock-out before an hour is completed if the tasks are completed? Do we need to clock-in and compulsorily complete 7 hours a week even if the tasks are completed?",
    "If the tasks are completed, there is no need to clock-in and clock-out unnecessarily for hours. However, you should keep a track of all the updates of the internship being posted on the groups.",
])

trainer.train([
    "Resource links not working. What to do? Should we skip?",
    "Please do not skip any piece of training, in case you're not able to access any link please message to Cloud Counselage HR and drop an email to hrsupport@cloudcounselage.in regarding the same.",
])

trainer.train([
    "What to do when our university exams start?",
    "We have provided our interns with preparatory leave from the exam season, nevertheless, you are free to work on your LP3 assignment, but we suggest to concentrate on your exams first.",
])

trainer.train([
    "Is it okay to mention this internship as ongoing for college records?",
    "Yes, we'll provide every intern a joining letter as soon as all interns are inducted. ",
])

trainer.train([
    "Can we do another internship with IP?",
    "Yes, you can do another internship outside of Cloud Counselage but please ensure to provide 1 hour a day or 7 hours a week for IP.",
])

trainer.train([
    "What to do after Live Projects? Are we getting an offer letter/Stipend?",
    "Submit your project and once it's reviewed as successful, collect your internship letter. Your internship is complete after this. There is no stipend for live projects. If your work is sublime and we have a vacancy in the position you're interested in, you may be offered a chance for interviews and can get an offer letter from Cloud Counselage Pvt. Ltd.",
])

trainer.train([
    "When will we get a joining letter? ",
    "Joining letter to all the interns will be provided on or before the 31st of March 2020.",
])

trainer.train([
    "When will we get an internship completion letter?",
    "This is a three (3) month internship conducted in the month of March, June & July 2020. You will receive your internship experience letter in August during the convocation only if you successfully submit your Live Project.",
])

trainer.train([
    "What will be the projects in AI/ ML/ etc. technologies in LP3/ Live Projects? ",
    "Projects in LP3 and Live Projects will be relevant to your training and ongoing projects in Cloud Counselage. The actual problem statements will only be given when the LP3/ Live Project phase is in progress to keep the interns focused on LP1/ LP2.",
])

trainer.train([
    "Not able to see the task as not part of the IP workgroup. ",
    "Please message ‘Cloud Counselage HR’ in Bitrix24 ",
])

trainer.train([
    "Live Project/ LP3 has to be submitted individually or it will be a group project? ",
    "All the LP3/  Live Projects are on an individual scale.",
])

trainer.train([
    "How can we check our weekly hours? ",
    "In the menu select 'time and reports' ->worktime and then you could see your worktime or click on this link once you’re logged in to Bitrix24; https://cloudcounselage24.bitrix24.com/timeman/timeman.php",
])

trainer.train([
    "Is it necessary to attend LP1 for other domains as well if we want to take its training. ",
    "LP1 training is common across all the technologies",
])

trainer.train([
    "Why only this training for LP2?",
    "They are our training partners and we have handpicked this training to cover a certain topic for you. These training cover from the very basic to intermediate level and is the perfect medium for you to have a starting point.",
])

trainer.train([
    "Could I have done this training from other websites/ resources?",
    "Yes, you could have but the reason to have these videos is to keep an enclosed environment for you to watch these tutorials without distractions with quizzes and forums for you to discuss in. As mentioned earlier, our main aim is to provide you with a starting point and baseline for the technology of your choice.",
])

trainer.train([
    "Can I do certification for the training provided in LP2? ",
    "Yes, Cloud Counselage has purposefully partnered with Edureka so as to enable our interns to get the advantage of the corporate benefits at 'no profit no loss' basis for Cloud Counselage, that we receive from the partnership. Being our interns, you can get huge discounts on the certifications you choose to enrol for through Cloud Counselage and Edureka. In case you want to know more about the discounts offered, please reach out to ‘Cloud Counselage HR’ or write to hrsupport@cloudcounselage.in.",
])

trainer.train([
    "The videos of LP2 are taking too much time to load.",
    "We have uploaded the videos of the highest quality and best resolution which has resulted in some videos being over 1 GB as they are of hours in duration. To experience these high definition videos we request you to wait at least 5 minutes or more; depending on your computer's RAM and internet connection.",
])

trainer.train([
    "Are LP1/ LP2/ LP3 a part of the Live Project?",
    "LP1/ LP2/ LP3 is your preparation for the Live Project. All the phases LP1/ LP2/ LP3/ Live Project are a part of this internship.",
])

trainer.train([
    "Will these training be enough for us to complete the LP3 and Live Project. ",
    "The set of training is not exhaustive and you are required to keep learning about the technology on your own to excel in your Live Project.",
])

trainer.train([
    "How do I access my quiz?",
    "As mentioned in the video: - Step1: Go to lp1 module Step2: Select module Step3: Put token (it will direct you to the home screen if the token is correct) Step4: Again go to lp1 module n select that module Step5: You will get the access by now Step6: Register there (each time for every module) Step7: Give the quiz Step8: Logout",
])

trainer.train([
    "By when will we receive access to Bitrix24?",
    " If you have submitted the ‘New Joinee Form’ after the 1st of March, please wait till the 31st of March to receive your access.",
])

trainer.train([
    "Can my friends still apply for the Internship Program (IP) - Maharashtra? Can we create awareness about this internship? Can we be the representative for Cloud Counselage in our college?",
    "Yes, your friends can apply till the 30th of March 2020; https://www.cloudcounselage.com/ipmaharashtra/. To be a student representative of Cloud Counselage, please contact Cloud Counselage HR.",
])

trainer.train([
    "Is the induction online or offline?",
    "As a precautionary measure to safeguard our intern’s health, we have decided to conduct all the inductions online.",
])

trainer.train([
    "I am trying to complete social media tasks. I completed that day and clicked finish but it didn't show finished in the task menu. What should I do?",
    "Our team will verify and then only your task shall be accepted as completed. Please wait till the verification's complete.",
])

trainer.train([
    "My Efficiency is 0% what should I do?",
    "Ensure that you have clicked ‘Start’ when you resume a task, the ‘Finish’ button gets active only after the task is started. Once you complete the task you can then click on ‘Finish’ and then the efficiency is updated in the system. However, please raise this issue with the Cloud Counselage HR, as they will look at it on a case to case basis.",
])

trainer.train([
    " Will you provide mentorship or doubt clearing sessions in this internship?",
    "As this is an internship you’re expected to do self-learning, mentorship is not part of an internship. However, we have created forums to resolve your doubts in the form of workgroups. As an intern ensure that you are part of relevant workgroups, i.e. ‘202003 - IP’ and your resp. Technology workgroup. In case, you are not a part of these workgroups, please reach out to ‘Cloud Counselage HR’ on Bitrix24 Chat.",
])

trainer.train([
    "Problem statements of the Live Project will be chosen by the intern or will be provided by Cloud Counselage?",
    "Live Projects will be provided by Cloud Counselage as these are the ongoing projects of Cloud Counselage and your opportunity to create an impact in the organisation.",
])

trainer.train([
    "Can we be a part of your future development team?/ Can we be hired by Cloud Counselage after this internship? ",
    "All our current interns if performing well in our internship programs can be offered an opportunity to interview for various positions in Cloud Counsealge. Many of our now full-time employees were interns in Cloud Counselage.",
])

trainer.train([
    "Can we visit the office? How many times do we have to visit the office for this internship?",
    "As this is an online internship you do not need to visit the offices in the duration of this internship. You will be requested to visit the Vikhroli office only once; i.e. on your internship convocation day which will be in July 2020. Nevertheless, you can visit our offices with an appointment.",
])

trainer.train([
    "Can we extend this internship? ",
    "Yes, you can extend your internship by being part of our other online programs like, ‘Online Career Program’.",
])

trainer.train([
    "If we are working on more than one technology, are those technologies added to the certificate? ",
    "You are not restricted from doing the training of other technologies but you will only be given an internship certificate of the technology you’re selected for.",
])

trainer.train([
    "Will Live Projects have only one technology or a mixture of technologies?",
    "Live Projects will have only your part of technology even if there are multiple technologies that are a part of the project, you will be working only on the part that covers your technology.",
])

trainer.train([
    "I forgot to clock in for a few days, will this affect my internship?",
    "This could have an adverse effect on your internship, please contact Cloud Counsealge HR and provide a genuine reason to miss clock in/ clock out. Also, please start performing your clock in/ clock out now.",
])

trainer.train([
    "Will I get LP3 and Live project of technology other than what I am selected for?",
    "No, you will receive LP3 and Live Projects of your respective technology.",
])

trainer.train([
    "I have not been added to the technology I preferred to work on?",
    "We do understand that you might be interested in other technologies and are eager to learn more, but we have prescribed the technologies based on your first inputs and cannot change your base technology. Nevertheless, you do have the opportunity to go through the training of all the technologies.",
])

trainer.train([
    "What are the company policies for IP interns?",
    "The company policies will be published on www.cloudcounselage.co.in/ippolicies",
])

trainer.train([
    "I have not got the acknowledgment from you regarding the weekly report.",
    "Once you submit your weekly report, your supervisor and the HR team shall take the cognizance. They would reach out to you in case of discrepancies, so you need not worry about the confirmation.",
])

trainer.train([
    "In my work time I can see one exclamation mark?/ What does the remaining time mean?",
    "It is showing the remaining time because it's configured for 8 working hours per day. Our interns need to only make sure that they are online for 1 hour per day or 7 hours a week.",
])

print("Talk to Bot. Write 'exit' to stop chatting.")
while True:
    query = input()
    if query == "exit":
        break
    answer = chatbot.get_response(query)
    print("Bot:",answer)