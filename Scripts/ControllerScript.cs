using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ControllerScript : MonoBehaviour
{
    public GameObject go;
    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        RaycastHit hit;
        transform.rotation = OVRInput.GetLocalControllerRotation(OVRInput.Controller.RTrackedRemote);

        if (Physics.Raycast(transform.position, transform.forward, out hit))
        {
            if(hit.collider != null) {
                if( go != hit.collider.gameObject)
                {
                    go = hit.transform.gameObject;
                    Debug.Log("On VR Raycast Enter");
                }
            }
        }
    }
}
