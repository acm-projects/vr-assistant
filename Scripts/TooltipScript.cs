using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TooltipScript : MonoBehaviour
{
    public Text helpText;
    public Text tooltipText;

    public string helpString;
    public string tooltipString;

    // Start is called before the first frame update
    void Start()
    {
        helpText = GameObject.Find("HelpText").GetComponent<Text>();
        tooltipText = GameObject.Find("tooltipText").GetComponent<Text>();
    }

    // Update is called once per frame
    void Update()
    {

    }
}
