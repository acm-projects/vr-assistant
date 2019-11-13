using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Text.RegularExpressions;
using System;
using UnityEngine.UI;

public class Login : MonoBehaviour
{
    public GameObject userName;
    public GameObject password;
    private string Username;
    private string Password;
    private string[] Lines;
    private string DecryptedPassword;

    public void LoginButton()
    {
        bool UN = false;
        bool PW = false;
        if(Username != "")
        {
            // HERE WE NEED TO CREATE A NEW FOLDER IN CHRISTINAS LAPTOP  AND REPLACE ALL INSTANCES OF WHAT I HAVE HERE WITH THAT FOLERS LOACTION
            // THIS IS 
            if(System.IO.File.Exists(@"C://UnityTestFolder/" + Username + ".txt"))
            {
                UN = true;
                Lines = System.IO.File.ReadAllLines(@"C://UnityTestFolder/" + Username + ".txt");
            }
            else
            {
                Debug.LogWarning("Username not found. Please try again!");
            }
        }
        else
        {
            Debug.LogWarning("Username Field is empty! Please try again");
        }
        if(Password != "")
        {
            if(System.IO.File.Exists(@"C://UnityTestFolder/" + Username + ".txt"))
            {
                
                int i = 1;
                foreach (char c in Lines[2])
                {
                    i++;
                    char Decrypted = (char)(c / i);
                    DecryptedPassword += Decrypted.ToString();
                }
                if(Password == DecryptedPassword)
                {
                    PW = true;
                }
                else
                {
                    Debug.LogWarning("Invalid Password");
                }
            }
            else
            {
                Debug.LogWarning("Invalid Password!");
            }

        }
        else
        {
            Debug.LogWarning("Password Field is empty!");
        }
        if(UN == true && PW == true)
        {
            userName.GetComponent<InputField>().text = "";
            password.GetComponent<InputField>().text = "";
            print("Login Succesful!");
            // Application.LoadLevel("insert scene");
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Tab))
        {
            if (userName.GetComponent<InputField>().isFocused)
            {
                password.GetComponent<InputField>().Select();
            }
        }

        if (Input.GetKeyDown(KeyCode.Return))
        {
            if (Username != "" && Password != "")
            {
                LoginButton();
            }
        }
        Username = userName.GetComponent<InputField>().text;
        Password = password.GetComponent<InputField>().text;
    }
}
