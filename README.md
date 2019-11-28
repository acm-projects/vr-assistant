# Mischa
Immersive assistant that helps you stay organized and responds with care and concern for your well being. Immersiveness is achieved by creating a room where you are situated in a desk - every time you log on - but are allowed to roam around your room while music plays in the back or, if you would prefer, view a virtual scenery through your windows.


## Features
### Voice to Text
Using the Google Cloud Speech-to-Text API, the user can speak to Mischa, who then responds with Google text-to-speech.
### Assistant Features
Using the Google DialogFlow API, users can trigger different intents when speaking to Mischa, as well as hold general conversation. These intents include scheduling with Google Calendar, a meditation intent, and a music intent.
### Sentiment Analysis
Using the Google Cloud Natural Language API, Mischa analyzes the user's language to determine their sentiment and keeps track of this value over time. Based on the user's sentiment, Mischa may suggest that the user uses our stress-reduction activities.
### Accessibility
Mischa fully supports seated users with dynamic height tracking and snap turns for an optimal viewing angle. Also features teleportation capabilities to help reduce motion sickness. The selection visualizer (pointer) and teleportation controls are accessible with both controllers.
### Stress Reduction Activities
Users can freely explore different scenes, practice archery, stream videos in a mini theater, and even create 3D sculptures using Mischa's built-in paintbrush. Users can also ask Mischa to play a meditation tape or music of their choice from YouTube.


## Dependencies
> Unity Editor 2.1.3

> Unity  Version: 2018.4.9f1 (LTS)

> Python 3.7

> Python packages: speech_recognition, playsound, gtts, pyaudio, google.cloud, dialogflow, selenium

> Assets: [SteamVR Plugin v1.2.3 [deprecated]](https://github.com/ValveSoftware/steamvr_unity_plugin/releases/tag/1.2.3)


## Built With
* [Unity](https://unity3d.com/get-unity/download) - Main Platform, Dependency Management
* [SteamVR Plugin](https://assetstore.unity.com/packages/tools/integration/steamvr-plugin-32647) - Archery, Painting
* [Oculus Integration](https://assetstore.unity.com/packages/tools/integration/oculus-integration-82022) - Control Mapping, Selection Visualizer
* [Virtual Reality Toolkit](https://github.com/ExtendRealityLtd/VRTK) - Teleportation, Snap Turns, Audio Spatialization
* [Blender](https://www.blender.org/) - Prefab Modeling
* [Google Cloud Natural Language API](https://cloud.google.com/natural-language/) - Sentiment Analysis
* [Google DialogFlow API](https://dialogflow.com/) - Conversation and intents
* [Google Calendar API](https://developers.google.com/calendar) - Scheduling Events
* [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/) - Speech Recognition
* [Google Cloud Text-to-Speech(https://cloud.google.com/text-to-speech/) - Converting text to speech
* [Flask](https://palletsprojects.com/p/flask/) - Used to call Python backend from C# in Unity
* [Selenium](https://selenium.dev/) - Used for getting music from YouTube


## Roadmap
Ideas for future implementation: 
* Expansion to other platforms (HTC Vive, Valve Index, Windows Mixed Reality) & mobile support (Google Cardboard)
* Advanced music functionality, where users can import songs/playlists, pause, queue, and shuffle songs
* Enhanced voice assistant compatibility (Google Assistant & Amazon Alexa)
* Environment customization, allowing users to adjust the furniture, lighting & import their own 3D models

## Authors
* **Yohan Flores** - *Project Manager* - [Pixel-Yohan](https://github.com/Pixel-Yohan)
* **Firstname Lastname** - *Role* - [Username](http://github.com/)


See also the list of [contributors](https://github.com/acm-projects/vr-assistant/graphs/contributors) who participated in this project.
