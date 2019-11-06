using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI; // Required when Using UI elements.

public class input_field : MonoBehaviour
{
    // Start is called before the first frame update
    //public InputField mainInputField;

    //public void Start()
    //{
    //    mainInputField.text = "Enter Text Here...";
    //}

    //public string stringToEdit = "Hello World";

    //void OnGUI()
    //{
    //    Make a text field that modifies stringToEdit.
    //   stringToEdit = GUI.TextField(new Rect(10, 10, 200, 20), stringToEdit, 25);
    //}
    public InputField time;
    public InputField eventName;
    public Text textDisplay;

    public void Setget()
    {
        textDisplay.text = "Time: " + time.text + "\nEvent: " + eventName;
    }

    private InputField input;
    void Awake()
    {
        input = GameObject.Find("Input Field").GetComponent<InputField>();
    }

    public void GetInput (string inputVal)
    {
        Debug.Log("User input: " + inputVal);
        input.text = "";
    }
    //void Start()
    //{
    //    //var input = gameObject.GetComponent<InputField>();
    //    //var se = new InputField.SubmitEvent();
    //    //se.AddListener(SubmitName);
    //    //input.onEndEdit = se;

    //    //or simply use the line below, 
    //    //input.onEndEdit.AddListener(SubmitName);  // This also works
    //}

    //private void SubmitName(string arg0)
    //{
    //    Debug.Log(arg0);
    //}

    //// Update is called once per frame
    //void Update()
    //{

    //}


}
