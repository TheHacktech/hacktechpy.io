//Location can be: “Field”, “Uni”, “Other”
//Days can be: “fri”, “sat”, “sun”
//start can be: [TIME][PERIOD]  ie “12:00AM”, “12:45PM”
//duration is duration in hours. ie 1 hour would be “1:00”

var schedule = [
{

// food

  title: "Dinner",
  caption: "Come enjoy some Teriyaki rice bowls and meet fellow hackers!",
  time: {day: "fri", start: "6:30PM", duration: "1:30"},
  location: "Bechtel",
  event_type: "Main timeline"
},
{
  title: "Midnight Snack",
  caption: "What's poppin, hackers! (Come enjoy fresh popcorn)!",
  time: {day: "sat", start: "12:30AM", duration: "1:00"},
  location: "Avery",
  event_type: "Main timeline"
},
{
  title: "Breakfast",
  caption: "Coffee, juice, muffins and fruit",
  time: {day: "sat", start: "5:00AM", duration: "5:00"},
  location: "Avery Outer Courtyard",
  event_type: "Main timeline"
},

{
  title: "Lunch",
  caption: "Scrumptious barbeque cooked with love by our lovely volunteers",
  time: {day: "sat", start: "11:30AM", duration: "1:30"},
  location: "Bechtel",
  event_type: "Main timeline"
},

{
  title: "Dinner",
  caption: "Pasta dinner cooked with love by our wonderful volunteers",
  time: {day: "sat", start: "6:30PM", duration: "2:00"},
  location: "Bechtel",
  event_type: "Main timeline"
},

{
  title: "Midnight Snack",
  caption: "Drink boba and chow down on eggrolls!",
  time: {day: "sun", start: "12:30AM", duration: "1:00"},
  location: "Bechtel",
  event_type: "Main timeline"
},

{
  title: "Donuts!",
  caption: "Enjoy some early morning donuts.",
  time: {day: "sun", start: "7:00AM", duration: "1:00"},
  location: "Bechtel",
  event_type: "Main timeline"
},

{
  title: "Lunch",
  caption: "Get hyped for project expo while enjoying In-N-Out!",
  time: {day: "sun", start: "11:00AM", duration: "1:00"},
  location: "Outside Avery",
  event_type: "Main timeline",
},


// workshops
{
  title: "[eBay] Innovation & Hacktech-Help Workshop",
  caption: "Come learn about innovation at eBay and how to get started working with eBay’s APIs. This session will kick-off with a short innovation docuseries which follows teams as they go through the Innovation Program at eBay. Afterwards, we’ll dive into a working session where you will learn about eBay’s public APIs and how to get started. We look forward to seeing you there!",
  time: {day: "fri", start: "9:00 PM", duration: "1:00"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "[Google Cloud] Three Powerful Google Cloud Products for Your Project",
  caption: "Come for a chat about Google Cloud computing and Google Cloud Platform! This talk highlights App Engine, Machine Learning APIs, and Cloud Firestore. For each product, there are interactive demos and example use cases. There will be door prizes (aka free shirts!)",
  time: {day: "fri", start: "11:30 PM", duration: "1:00"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "[Esri] Maps and Location Services",
  caption: "Discover how to use maps and services to change the world. Learn about 2D and 3D technology, geocoding, routing, and other technologies.",
  time: {day: "sat", start: "1:00 AM", duration: "1:00"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "Hacking the NASA JPL Way: Solving Space Challenges",
  caption: "Meet astronaut Larry James! He is currently the deputy director of NASA’s Jet Propulsion Laboratory and he will be speaking about his incredible experiences in solving space challenges.",
  time: {day: "sat", start: "8:45 AM", duration: "1:00"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "[Oracle] Build Cloud-Native Applications with Oracle Cloud",
  caption: "Come and join us to see how you too can build cloud-native applications on Oracle Cloud. We will take you through the journey of MuShop, a fully cloud-native, microservices based online shop. You will discover how to leverage cloud technology to build leading-edge applications for the world of tomorrow.",
  time: {day: "sat", start: "10:00 AM", duration: "1:00"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
	title: "[Keystone Strategy] Turning Data into a Story: The Secret Tales of Commit Logs",
  caption: "In today's world, data is created everywhere - including in your codebase. Good developers track projects with work planning tools and tickets, and that tracking can create a host of information contained within version control software and the code itself. At Keystone Strategy, we are often working to turn data into a story, and commit logs are goldmine. Understanding how to extract information and a project narrative from codebases allows us to understand the environmental factors altering project development and better inform our clients development narrative. Join us as we teach your teams how to analyze your projects to find insights about your working style and the projects development history.",
  time: {day: "sat", start: "11:00 AM", duration: "0:30"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "How to Host Your Web App on the Cloud for Free",
  caption: "Caltech student Alex Cui will lead this workshop on hosting a web app publically on the cloud!",
  time: {day: "sat", start: "1:00 PM", duration: "1:00"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "Mental Health",
  caption: "Caltech Professor Adam Blank will speak about mental health.",
  time: {day: "sat", start: "2:00 PM", duration: "1:00"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "[Office Ally] Office Ally Q & A",
  caption: "Come ask any questions about Office Ally, and meet Chief Technology Officer (and keynote speaker) Jay Wu, and Development Deployment Manager David Liljeblad.",
  time: {day: "sat", start: "3:00 PM", duration: "0:30"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "[Keystone Strategy] The AI Impact: How Technology is Changing Business Decisions",
  caption: "It should come as no surprise that artificial intelligence and machine learning are reshaping the business landscape, but where do these technical investments create the most impact? Join us as we review the current and potential value these technologies create across industries, based on the latest work from Harvard Business School Digital Innovation Chair Marco Iansiti. We will take a deeper dive into how these technologies are driving business decision making, and discuss how you can leverage this to create maximum impact via your hacks. ",
  time: {day: "sat", start: "5:00 PM", duration: "0:30"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "SpatialDB: Enabling Rigorous Geospatial Queries",
  caption: "Come hear Caltech student Rupesh Jeyaram speak about his research project on building spatial databases to access, explore, and navigate the terabytes of data. ",
  time: {day: "sat", start: "5:30 PM", duration: "0:45"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
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

{
  title: "Registration",
  caption: "Welcome to Hacktech! Come check-in and grab some swag!",
  time: {day: "fri", start: "6:00PM", duration: "2:30"},
  location: "Avery",
  event_type: "events"
},

{
  title: "Snack Mix & Mingle",
  caption: "Come grab some snacks and mingle with other hackers!",
  time: {day: "fri", start: "8:00PM", duration: "1:00"},
  location: "Avery",
  event_type: "events"
},
{
  title: "Opening Ceremony",
  caption: "Get hyped for Hacktech 2020!",
  time: {day: "fri", start: "10:00PM", duration: "1:00"},
  location: "Beckman Auditorium",
  event_type: "events",
},

{
  title: "Team Building",
  caption: "Find a team to work with!",
  time: {day: "fri", start: "11:00PM", duration: "1:00"},
  location: "Beckman Auditorium",
  event_type: "events"
},

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

{
  title: "Project Expo",
  caption: "Show off your fantastic new hack!",
  time: {day: "sun", start: "12:00PM", duration: "2:00"},
  location: "Avery",
  event_type: "events",
},

{
  title: "Closing Ceremony",
  caption: "Winners are announced! Come see the winning teams demo on stage!",
  time: {day: "sun", start: "2:30PM", duration: "1:30"},
  location: "Beckman Auditorium",
  event_type: "events",
},

{
  title: "Buses Depart",
  caption: "Thanks for coming!",
  time: {day: "sun", start: "4:00PM", duration: "1:00"},
  location: "",
  event_type: "events",
},

]
