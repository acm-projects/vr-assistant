using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//public class AudioSource_Play : MonoBehaviour
//{
//    // Start is called before the first frame update
//    void Start()
//    {

//    }

//    // Update is called once per frame
//    void Update()
//    {

//    }
//}

// Allow a song to be chosen and played.  If can be paused, and the song played further.
// Two songs are supported.


[RequireComponent(typeof(AudioSource))]
public class AudioSource_Play : MonoBehaviour
{
    // two clips, perhaps songs for the game
    public AudioClip song1;
    public AudioClip song2;

    private AudioSource audioSource;
    private bool paused1;
    private bool paused2;

    // both songs are in paused state
    void Start()
    {
        audioSource = GetComponent<AudioSource>();
        paused1 = true;
        paused2 = true;
    }

    void OnGUI()
    {
        if (GUI.Button(new Rect(10, 10, 150, 75), "Play Calm Song"))
        {
            if (paused1 && paused2)
            {
                audioSource.clip = song1;
                audioSource.Play(0);
                paused1 = false;
            }
        }

        if (GUI.Button(new Rect(200, 10, 150, 75), "Pause Calm Song"))
        {
            if (paused1 == false)
            {
                audioSource.Pause();
                paused1 = true;
            }
        }

        if (GUI.Button(new Rect(10, 130, 150, 75), "Play Happy Song"))
        {
            if (paused2 && paused1)
            {
                audioSource.clip = song2;
                audioSource.Play(0);
                paused2 = false;
            }
        }

        if (GUI.Button(new Rect(200, 130, 150, 75), "Pause Happy Song"))
        {
            if (paused2 == false)
            {
                audioSource.Pause();
                paused2 = true;
            }
        }
    }
}
////This script allows you to toggle music to play and stop.
////Assign an AudioSource to a GameObject and attach an Audio Clip in the Audio Source. Attach this script to the GameObject.

//public class AudioSource_Play : MonoBehaviour
//{
//    AudioSource m_MyAudioSource;

//    //Play the music
//    bool m_Play;
//    //Detect when you use the toggle, ensures music isn’t played multiple times
//    bool m_ToggleChange;

//    void Start()
//    {
//        //Fetch the AudioSource from the GameObject
//        m_MyAudioSource = GetComponent<AudioSource>();
//        //Ensure the toggle is set to true for the music to play at start-up
//        m_Play = true;
//    }

//    void Update()
//    {
//        //Check to see if you just set the toggle to positive
//        if (m_Play == true && m_ToggleChange == true)
//        {
//            //Play the audio you attach to the AudioSource component
//            m_MyAudioSource.Play();
//            //Ensure audio doesn’t play more than once
//            m_ToggleChange = false;
//        }
//        //Check if you just set the toggle to false
//        if (m_Play == false && m_ToggleChange == true)
//        {
//            //Stop the audio
//            m_MyAudioSource.Stop();
//            //Ensure audio doesn’t play more than once
//            m_ToggleChange = false;
//        }
//    }

//    void OnGUI()
//    {
//        //Switch this toggle to activate and deactivate the parent GameObject
//        m_Play = GUI.Toggle(new Rect(10, 10, 100, 30), m_Play, "Play Music");

//        //Detect if there is a change with the toggle
//        if (GUI.changed)
//        {
//            //Change to true to show that there was just a change in the toggle state
//            m_ToggleChange = true;
//        }
//    }
//}
//}
