//Location can be: “Field”, “Uni”, “Other”
//Days can be: “fri”, “sat”, “sun”
//start can be: [TIME][PERIOD]  ie “12:00AM”, “12:45PM”
//duration is duration in hours. ie 1 hour would be “1:00”

var schedule = [
{

// food

  title: "Dinner",
  caption: "",
  time: {day: "fri", start: "6:00PM", duration: "2:00"},
  location: "Bechtel",
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
  time: {day: "sat", start: "11:00AM", duration: "2:00"},
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
  time: {day: "sun", start: "6:00AM", duration: "1:00"},
  location: "Chandler",
  event_type: "Main timeline"
},

{
  title: "Brunch",
  caption: "",
  time: {day: "sun", start: "9:00AM", duration: "3:00"},
  location: "Chandler",
  event_type: "Main timeline",
},


// workshops
{
  title: "Sponsor Workshop",
  caption: "TBA",
  time: {day: "fri", start: "8:00 PM", duration: "1:00"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "Sponsor Workshop",
  caption: "TBA",
  time: {day: "fri", start: "11:30 PM", duration: "1:00"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "Hacking the NASA JPL Way: Solving Space Challenges",
  caption: "Meet astronaut Larry James!",
  time: {day: "sat", start: "8:45 AM", duration: "1:00"},
  location: "Annenberg 105",
  event_type: "Workshops"
},
{
  title: "How to Host Your Web App on the Cloud for Free",
  caption: "Alex Cui",
  time: {day: "sat", start: "1:00 PM", duration: "1:00"},
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
  time: {day: "fri", start: "9:00PM", duration: "1:00"},
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
