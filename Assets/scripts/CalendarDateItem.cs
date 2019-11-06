using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class CalendarDateItem : MonoBehaviour {

    public InputField time;
    public InputField eventName;
    public Text textDisplay;
    public void OnDateItemClick()
    {
        CalendarController._calendarInstance.OnDateItemClick(gameObject.GetComponentInChildren<Text>().text);
        textDisplay.text = "Time: " + time.text;
        textDisplay.text += "\nEvent: " + eventName;
    }
}
