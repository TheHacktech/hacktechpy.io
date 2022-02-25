//Location can be: “Field”, “Uni”, “Other”
//Days can be: “fri”, “sat”, “sun”
//start can be: [TIME][PERIOD]  ie “12:00AM”, “12:45PM”
//duration is duration in hours. ie 1 hour would be “1:00”

var schedule = [
  // workshops
  {
    title: "Blocktech Workshop: Blockchain and Solidity Fundamentals",
    caption: "Learn how to develop on the Ethereum blockchain using Solidity!",
    time: { day: "fri", start: "10:00 PM", duration: "1:00" },
    location: "twitch",
    event_type: "Workshops",
  },
  {
    title: "What they don't tell you about tech interviews",
    caption:
      "Are you terrified of the tech interview process? Do you wish someone could just give you an end-to-end overview of what the whole process is like? Or are you someone who’s very frustrated with how you just don’t seem to understand what the interviewer wants? You get interviews and you seem to do everything right on paper, but something’s still amiss? If you find yourself saying yes to any of these questions, then this workshop is for you. In this workshop, we’ll walkthrough the tech interview process, including the art of networking during COVID, the standard tech interview process, tips and tricks for behavioural and technical rounds which go beyond just getting the question right and that’ll really help you stand out as a candidate, post-interview etiquette, compensation packages and negotiation etc. The best part? I recently went through this process myself so you’ll also get to hear the silly mistakes that I made along the way and what I learnt as I went along!",
    time: { day: "sat", start: "10:00 AM", duration: "1:00" },
    location: "twitch",
    event_type: "Workshops",
  },
  {
    title: "AeroVect Tech Talk",
    caption: "TBD!",
    time: { day: "sat", start: "11:00 AM", duration: "1:00" },
    location: "twitch",
    event_type: "Workshops",
  },
  {
    title: "Boarding the Intern Ship",
    caption:
      "All aboard the intern ship!!! In this talk, Robert will discuss how to find an internship, what to look for in a job, and what adulting is like. Come with existential crises about what to do with your life and career and we'll sort through the mess.",
    time: { day: "sat", start: "1:00 PM", duration: "1:00" },
    location: "twitch",
    event_type: "Workshops",
  },
  {
    title: "JPL Speaker Talk",
    caption: "TBD!",
    time: { day: "sat", start: "2:00 PM", duration: "1:00" },
    location: "twitch",
    event_type: "Workshops",
  },
  {
    title: "1517 Fund Office Hours",
    caption: "TBD!",
    time: { day: "sat", start: "5:00 PM", duration: "2:00" },
    location: "discord + zoom",
    event_type: "Workshops",
  },

  // events
  {
    title: "Opening Ceremony + Keynote",
    caption: "TBD!",
    time: { day: "fri", start: "7:30 PM", duration: "1:00" },
    location: "twitch",
    event_type: "events",
  },
  {
    title: "Team Matching",
    caption: "TBD!",
    time: { day: "fri", start: "8:30 PM", duration: "1:00" },
    location: "zoom + Glimpse",
    event_type: "events",
  },
  {
    title: "Kahoot Tournament",
    caption: "TBD!",
    time: { day: "sat", start: "12:00 AM", duration: "1:00" },
    location: "twitch",
    event_type: "events",
  },
  {
    title: "Chess Tournament",
    caption: "TBD!",
    time: { day: "sat", start: "3:30 PM", duration: "1:30" },
    location: "discord",
    event_type: "events",
  },
  {
    title: "Poker Tournament",
    caption: "TBD!",
    time: { day: "sat", start: "8:00 PM", duration: "1:00" },
    location: "discord",
    event_type: "events",
  },
  {
    title: "skribbl.io Tournament",
    caption: "TBD!",
    time: { day: "sun", start: "12:00 AM", duration: "1:00" },
    location: "discord",
    event_type: "events",
  },
  {
    title: "Judging",
    caption: "Judges will hold calls with all hackers to choose finalists",
    time: { day: "sun", start: "12:00 PM", duration: "1:30" },
    location: "discord",
    event_type: "events",
  },
  {
    title: "Finalist Judging",
    caption: "Judges will hold calls with finalists to choose winners",
    time: { day: "sun", start: "2:00 PM", duration: "0:30" },
    location: "discord",
    event_type: "events",
  },
  {
    title: "Closing Ceremony",
    caption: "Winners are announced! Tune in to see winning team's demos!",
    time: { day: "sun", start: "3:00 PM", duration: "1:30" },
    location: "twitch",
    event_type: "events",
  },
  /*
  {
    title: "Speedfriending!",
    caption: "",
    time: { day: "fri", start: "10:00 PM", duration: "0:30" },
    location: "zoom",
    event_type: "events",
  },
  {
    title: "Chess Tournament",
    caption: "",
    time: { day: "sat", start: "11:30 AM", duration: "1:30" },
    location: "zoom",
    event_type: "events",
  },
  {
    title: "Drop-in Game Night!",
    caption: "",
    time: { day: "sat", start: "5:00 PM", duration: "1:00" },
    location: "zoom",
    event_type: "events",
  },
  {
    title: "Poker Tournament",
    caption: "",
    time: { day: "sat", start: "8:00 PM", duration: "1:00" },
    location: "zoom",
    event_type: "events",
  },
  {
    title: "International's Mixer",
    caption: "Come talk with fellow international students!",
    time: { day: "sat", start: "9:00 PM", duration: "0:30" },
    location: "zoom",
    event_type: "events",
  },
  {
    title: "Judging",
    caption: "Judges will hold calls with all hackers to choose finalists",
    time: { day: "sun", start: "12:00PM", duration: "1:30" },
    location: "discord",
    event_type: "events",
  },
  {
    title: "Finalist Judging",
    caption: "Judges will hold calls with finalists to choose winners",
    time: { day: "sun", start: "2:00PM", duration: "0:30" },
    location: "discord",
    event_type: "events",
  },
  {
    title: "Closing Ceremony",
    caption: "Winners are announced! Tune in to see winning team's demos!",
    time: { day: "sun", start: "3:00PM", duration: "1:30" },
    location: "zoom",
    event_type: "events",
  },
  */
];
/*
  // old workshops 2021
  {
    title: "echoAR: How to Build a Cloud-Connected AR/VR App in 15 Minutes or Less",
    caption: "The workshop will show how to quickly create augmented and virtual reality (AR/VR) apps with no technical skills or coding required and scale existing apps by connecting them to the cloud. Workshop participants will learn how to create real-time cloud-connected AR/VR apps using the echoAR platform. Participants will also discover how AR/VR are changing the world through the demonstration of different use cases of 3D applications and live demos of AR/VR experiences. Participants are encouraged to bring a laptop and a smartphone. Platforms for experimentation include: Google ARCore, WebXR, Vuforia, Unity-based apps, and more.",
    time: {day: "fri", start: "10:00 PM", duration: "1:00"},
    location: "echoAR channel in discord",
    event_type: "Workshops"
  },
  {
    title: "How to host your web app publically on the cloud for free",
    caption: "Learn how to easily build with one the most popular, modern web stacks, using Nginx, Node.js Express, and Let's Encrypt, to make your web app public and legit!",
    time: {day: "fri", start: "11:00 PM", duration: "1:00"},
    location: "zoom",
    event_type: "Workshops"
  },
  {
    title: "Leading Virtualitics",
    caption: "The story of the journey of a AI-driven data analytics startup (who just raised their Series B!)",
    time: {day: "sat", start: "11:00 AM", duration: "0:30"},
    location: "zoom",
    event_type: "Workshops"
  },
  {
    title: "Kyle Bebak's Tech Talk",
    caption: "Building/consuming web APIs is fundamental to web and mobile development. HTTP clients make working with web APIs a lot easier. Roughly speaking, HTTP clients fall into two categories: GUI apps, like Postman, Insomnia and Paw, and CLI apps like cURL and HTTPie. Requester is an HTTP client for Sublime Text. It combines the \"managed UI\" features from GUI clients like collections, request history, env vars, syntax highlighting, request chaining, etc, with the speed of CLI clients. Everything is text, so sharing and versioning request collections is trivial. It uses [Requests' syntax](http://docs.python-requests.org/en/master/), which is very nice and well documented. I'd also like to show you how Requester works, some of the cool things it does with Python, how it uses Sublime Text to build a UI that combines the best of GUI and CLI, and how it could be improved by incorporating some \"newish\" Python features.",
    time: {day: "sat", start: "1:00 PM", duration: "1:00"},
    location: "zoom",
    event_type: "Workshops"
  },
  {
    title: "JPL Workshop: Delay Tolerant Networking",
    caption: "Learn the protocols for Space Internet and use the Delay Tolerant Networking’s Interplanetary Overlay Network tools in your Hacktech Project!! <a href='https://github.com/carlynlee/dtndocker'>GitHub repo</a>",
    time: {day: "sat", start: "2:00 PM", duration: "1:00"},
    location: "zoom",
    event_type: "Workshops"
  },
  {
    title: "Google Cloud Talk: Intro to Firebase",
    caption: "",
    time: {day: "sat", start: "3:00 PM", duration: "1:00"},
    location: "<a href='http://meet.google.com/bvz-svsd-pbo'>http://meet.google.com/bvz-svsd-pbo</a>",
    event_type: "Workshops"
  },
  {
    title: "Miso Robotics",
    caption: "Ryan Sinnet is the CTO of Miso Robotics, an AI Robotics startup that developed Flippy, the world's first AI-power robotic kitchen assistant that can flip burgers and fry foods! We'll hear about his journey as a CTO, what he's learned, and what's the future looks like for autonomous chefs.",
    time: {day: "sat", start: "4:00 PM", duration: "1:00"},
    location: "zoom",
    event_type: "Workshops"
  },
  {
    title: "Techreach",
    caption: "Learn about diversity and inclusion in tech and how techreach is involved.",
    time: {day: "sat", start: "6:00 PM", duration: "1:00"},
    location: "zoom",
    event_type: "Workshops"
  },
  */
/*
  {
    title: "[eBay] Innovation & Hacktech-Help Workshop",
    caption: "Come learn about innovation at eBay and how to get started working with eBay’s APIs. This session will kick-off with a short innovation docuseries which follows teams as they go through the Innovation Program at eBay. Afterwards, we’ll dive into a working session where you will learn about eBay’s public APIs and how to get started. We look forward to seeing you there!",
    time: {day: "fri", start: "9:00 PM", duration: "1:00"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  {
    title: "[Google Cloud] Three Powerful Google Cloud Products for Your Project",
    caption: "Come for a chat about Google Cloud computing and Google Cloud Platform! This talk highlights App Engine, Machine Learning APIs, and Cloud Firestore. For each product, there are interactive demos and example use cases.",
    time: {day: "fri", start: "11:00 PM", duration: "1:00"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  {
    title: "[Esri] Maps and Location Services",
    caption: "Discover how to use maps and services to change the world. Learn about 2D and 3D technology, geocoding, routing, and other technologies.",
    time: {day: "sat", start: "12:00 AM", duration: "1:00"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  {
    title: "Hacking the NASA JPL Way: Solving Space Challenges",
    caption: "Meet astronaut Larry James! He is currently the deputy director of NASA’s Jet Propulsion Laboratory and he will be speaking about his incredible experiences in solving space challenges.",
    time: {day: "sat", start: "9:00 AM", duration: "1:00"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  {
    title: "[Oracle] Build Cloud-Native Applications with Oracle Cloud",
    caption: "Come and join us to see how you too can build cloud-native applications on Oracle Cloud. We will take you through the journey of MuShop, a fully cloud-native, microservices based online shop. You will discover how to leverage cloud technology to build leading-edge applications for the world of tomorrow.",
    time: {day: "sat", start: "10:00 AM", duration: "1:00"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  {
    title: "[Keystone Strategy] Turning Data into a Story: The Secret Tales of Commit Logs",
    caption: "In today's world, data is created everywhere - including in your codebase. Good developers track projects with work planning tools and tickets, and that tracking can create a host of information contained within version control software and the code itself. At Keystone Strategy, we are often working to turn data into a story, and commit logs are goldmine. Understanding how to extract information and a project narrative from codebases allows us to understand the environmental factors altering project development and better inform our clients development narrative. Join us as we teach your teams how to analyze your projects to find insights about your working style and the projects development history.",
    time: {day: "sat", start: "11:00 AM", duration: "0:30"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  {
    title: "How to Host Your Web App on the Cloud for Free",
    caption: "Caltech student Alex Cui will lead this workshop on hosting a web app publicly on the cloud!",
    time: {day: "sat", start: "1:00 PM", duration: "1:00"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  {
    title: "Points Don’t Matter: Invest in Yourself, Not Your Grades",
    caption: "Mental health advice from Caltech's CS faculty and how to succeed after college.",
    time: {day: "sat", start: "2:00 PM", duration: "1:00"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  {
    title: "[Office Ally] Office Ally Q & A",
    caption: "Come ask any questions about Office Ally, and meet Chief Technology Officer (and keynote speaker) Jay Wu, and Development Deployment Manager David Liljeblad.",
    time: {day: "sat", start: "3:00 PM", duration: "0:30"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  {
    title: "[Keystone Strategy] The AI Impact: How Technology is Changing Business Decisions",
    caption: "It should come as no surprise that artificial intelligence and machine learning are reshaping the business landscape, but where do these technical investments create the most impact? Join us as we review the current and potential value these technologies create across industries, based on the latest work from Harvard Business School Digital Innovation Chair Marco Iansiti. We will take a deeper dive into how these technologies are driving business decision making, and discuss how you can leverage this to create maximum impact via your hacks. ",
    time: {day: "sat", start: "5:00 PM", duration: "0:30"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  {
    title: "Breaking the Billion Datapoint Barrier",
    caption: "Come hear Caltech student Rupesh Jeyaram speak about his research: With the rise of ubiquitous sensors, satellites, and devices, rapid information retrieval becomes paramount for both technological innovation and scientific research. Come by to learn about techniques that make data extraction, analysis, and visualization in large datasets tractable. I will use Python and SQL in the presentation, but no prior knowledge of either of these languages needed!",
    time: {day: "sat", start: "5:30 PM", duration: "0:45"},
    location: "Streamed on our channel!",
    event_type: "Workshops"
  },
  */
/*
  {
    title: "Using Cognitive Services to Uncover Your GoT House Pt. 1",
    caption: "Microsoft",
    time: {day: "fri", start: "11:00PM", duration: "1:00"},
    location: "Annenberg 105",
    event_type: "Workshops"
  },
    
  {
    title: "Machine Learning with AWS ML",
    caption: "Amazon",
    time: {day: "sat", start: "11:00AM", duration: "1:00"},
    location: "Annenberg 105",
    event_type: "Workshops"
  },
  
  {
    title: "Using Cognitive Services to Uncover Your GoT House Pt. 2",
    caption: "Microsoft",
    time: {day: "sat", start: "12:00AM", duration: "1:00"},
    location: "Annenberg 105",
    event_type: "Workshops"
  },
  
  {
    title: "Code for Ca$hflow w/ eBay APIs",
    caption: "Dan Fain, fellow ‘Tech-er and VP of Data Platform Engineering, and team will give you a download about transformative tech at eBay…and how you can turn your code into cashflow through their APIs.",
    time: {day: "sat", start: "1:00AM", duration: "1:00"},
    location: "Annenberg 105",
    event_type: "Workshops"
  },
  
  {
    title: "Build-a-(Slack)bot Workshop",
    caption: "Learn how to build a Slack bot for your hack!",
    time: {day: "sat", start: "2:00AM", duration: "1:00"},
    location: "Annenberg 105",
    event_type: "Workshops"
  },
  
  {
    title: "1517 Fund Office Hours",
    caption: "Meet with Nick Arnett from 1517 Fund and talk about your project! Check Slack to schedule a meeting.",
    time: {day: "sat", start: "1:00PM", duration: "4:00"},
    location: "Red Door Cafe",
    event_type: "Workshops"
  },
  
  {
    title: "How to Board the Intern Ship",
    caption: "Hack the internship and job hunting process.",
    time: {day: "sat", start: "5:00PM", duration: "1:00"},
    location: "Annenberg 105",
    event_type: "Workshops"
  },
  
  {
    title: "Disney Office Hours",
    caption: "Grab some Hacktech dinner and come chat with Disney!",
    time: {day: "sat", start: "6:00PM", duration: "1:00"},
    location: "Chandler Bar",
    event_type: "Workshops"
  },
  */

// Events
/*
  {
    title: "Registration",
    caption: "Welcome to Hacktech! Come check-in and grab some swag!",
    time: {day: "fri", start: "6:00PM", duration: "2:30"},
    location: "Avery",
    event_type: "events"
  },
  */
/*
  {
    title: "Snack Mix & Mingle",
    caption: "Come grab some snacks and mingle with other hackers!",
    time: {day: "fri", start: "8:00PM", duration: "1:00"},
    location: "Avery",
    event_type: "events"
  },
  */
/*
  {
    title: "Ice Breakers!",
    caption: "Get to know your fellow Hacktech hackers and sponsors through fun icebreakers!! Introductions + Two Truths and A Lie on Slack.",
    time: {day: "fri", start: "8:00PM", duration: "1:00"},
    location: "Slack channel",
    event_type: "events",
  },
  {
    title: "Opening Ceremony",
    caption: "Get hyped for Hacktech 2020!",
    time: {day: "fri", start: "10:00PM", duration: "1:00"},
    location: "Streamed on our channel!",
    event_type: "events",
  },
  {
    title: "Hacktech Online Chess Tournament",
    caption: "Compete against other Hacktech participants in online chess tournament (Blitz Time Control). Please see Workshops and Events link for more details on how to enter. There will be awesome prizes!",
    time: {day:"sat", start:"3:00PM", duration:"2:00"},
    location: "lichess.org",
    event_type: "events"
  },
  {
    title: "Capture the Flag Cybersecurity Challenge",
    caption: "Hosted by MLH -- fun challenge to learn about basic cybersecurity!",
    time: {day:"sat", start:"7:00PM", duration:"1:00"},
    location: "Slack channel",
    event_type: "events"
  },
  {
    title: "Kahoot! Trivia Game",
    caption: "Come join us for three rounds of trivia through Kahoot! The themes will be: Caltech, pop culture, and trivia about our sponsors, with prizes for the winners of each round!",
    time: {day:"sat", start:"8:00PM", duration:"1:00"},
    location: "Streamed on our channel!",
    event_type: "events"
  },
  {
    title: "League 5v5 Stream",
    caption: "5v5, organizers vs hackers League of Legends! See you on Summoner's Rift!",
    time: {day:"sat", start:"9:30PM", duration:"1:00"},
    location: "Streamed on our channel!",
    event_type: "events"
  },
  */
/*
  {
    title: "Team Building",
    caption: "Find a team to work with!",
    time: {day: "fri", start: "11:00PM", duration: "1:00"},
    location: "Beckman Auditorium",
    event_type: "events"
  },
  */
/*
  {
    title: "Puppy Party!",
    caption: "Take a break and come play with these adorable bundles of joy!",
    time: {day:"sat", start:"3:00PM", duration:"1:00"},
    location: "Avery Garage",
    event_type: "events"
  },
  
  {
    title: "Ultimate Frisbee",
    caption: "Get in some physical activity and come learn how to throw a frisbee, or come play a pick-up game! All skill levels welcome!",
    time: {day:"sat", start:"1:00PM", duration:"1:30"},
    location: "Beckman Lawn",
    event_type: "events"
  },
  
  {
    title: "Capture the Flag",
    caption: "Hosted by MLH.",
    time: {day:"sat", start:"7:00PM", duration:"1:00"},
    location: "Avery Conference",
    event_type: "events"
  },
  {
    title: "Werewolf",
    caption: "Find the werewolves among yourselves! Hosted by MLH.",
    time: {day:"sat", start:"8:00PM", duration:"1:00"},
    location: "Avery Conference",
    event_type: "events"
  },
  */

// {
//   title: "5-Hour Energy",
//   caption: "",
//   time: {day:"sat", start:"7:00PM", duration:"3:00"},
//   location: "Winnett",
//   event_type: "events",
// },

// {
//   title: "Cup Stacking with Swift",
//   caption: "",
//   time: {day:"sat", start:"10:00PM", duration:"1:00"},
//   location: "Winnett",
//   event_type: "events",
// },
//
// {
//   title: "Watermelon Eating Contest",
//   caption: "",
//   time: {day: "sat", start: "12:30PM", duration: "1:00"},
//   location: "Avery Courtyard",
//   event_type: "events"
// },
//
// {
//   title: "Life-size Jenga",
//   caption: "",
//   time: {day: "sat", start: "2:00PM", duration: "1:00"},
//   location: "Winnett",
//   event_type: "events"
// },
//
// {
//   title: "Minesweeper Tournament",
//   caption: "",
//   time: {day: "sat", start: "5:30PM", duration: "1:30"},
//   location: "Winnett",
//   event_type: "events"
// },
//
// {
//   title: "Anime Watching Party",
//   caption: "",
//   time: {day: "sat", start: "8:00PM", duration: "2:00"},
//   location: "Winnett",
//   event_type: "events"
// },
//
// {
//   title: "Powerade Contest?",
//   caption: "",
//   time: {day: "sat", start: "11:15PM", duration: "0:45"},
//   location: "Chandler",
//   event_type: "events"
// },
//
// {
//   title: "Bubble Wraaap *pop*",
//   caption: "",
//   time: {day: "sun", start: "1:00AM", duration: "1:00"},
//   location: "Winnett",
//   event_type: "events"
// },
/*
  {
    title: "Project Expo",
    caption: "Judges will view the video demos of your fantastic hacks through your Devpost submission!",
    time: {day: "sun", start: "10:30AM", duration: "2:00"},
    location: "Devpost",
    event_type: "events",
  },
  {
    title: "Finalist Judging",
    caption: "Judges will hold calls with finalists to choose winners - be sure to keep this block clear on your schedule in case you're chosen as a finalist!",
    time: {day: "sun", start: "12:30PM", duration: "2:00"},
    location: "Online",
    event_type: "events",
  },
  
  {
    title: "Closing Ceremony",
    caption: "Winners are announced! Tune in to see winning team's demos!",
    time: {day: "sun", start: "3:00PM", duration: "1:00"},
    location: "Streamed on our channel!",
    event_type: "events",
  },
  */
/*
  {
    title: "Buses Depart",
    caption: "Thanks for coming!",
    time: {day: "sun", start: "4:00PM", duration: "1:00"},
    location: "",
    event_type: "events",
  },
  */
