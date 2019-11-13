using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.Text.RegularExpressions;

public class Register : MonoBehaviour
{
    public GameObject userName;
    public GameObject email;
    public GameObject password;
    public GameObject confirmPassword;
    private string Username;
    private string Email;
    private string Password;
    private string ConfPassword;
    private string form; // hold the above 4 private variables
    private bool EmailValid = false;
    private string[] Characters = {"a","b","c","d","e","f","g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
        "E", "F", "G", "H", "I", "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
        "1","2","3","4","5","6","7","8","9","0","_","-" };
    

    public void RegisterButton() {
        bool UN = false;
        bool EM = false;
        bool PW = false;
        bool CPW = false;
        
        // Checks to make sure username isn't already taken
        if (Username != "")
        {
            if (!System.IO.File.Exists(@"C://UnityTestFolder/" + Username + ".txt"))
            {
                UN = true;
            }
            else
            {
                Debug.LogWarning("Username Taken");
            }
        }
        else {
            Debug.LogWarning("Username field Empty");
        }
        // Checks if Email is valid
        if(Email != "")
        {
            EmailValidation();
            if (EmailValid)
            {
                if (Email.Contains("@"))
                {
                    if (Email.Contains("."))
                    {
                        EM = true;
                    }
                    else
                    {
                        Debug.LogWarning("Email is incorrect");
                    }
                }
                else
                {
                    Debug.LogWarning("Email is incorrect");
                }
            }
            else
            {
                Debug.LogWarning("Email is incorrect");
            }
        }
        else
        {
            Debug.LogWarning("Email field is empty");
        }
        // Checks if password is valid
        if(Password != "")
        {
            if(Password.Length > 5)
            {
                PW = true;
            }
            else
            {
                Debug.LogWarning("Password Must be atleast 6 characters long!");
            }
        }
        else
        {
            Debug.LogWarning("Password field is empty!");
        }

        if(ConfPassword != "")
        {
            if (ConfPassword == Password)
            {
                CPW = true;
            }
            else {
                Debug.LogWarning("Passwords don't match!");
            }            
        }
        else
        {
            Debug.LogWarning("Confirm Password field is empty");
        }
        // This encrypts the password so that its safe
        if(UN == true&& EM == true && PW == true && CPW == true)
        {
            bool clear = true;
            int i = 1;
            foreach(char c in Password)
            {
                if(clear == true)
                {
                    Password = "";
                    clear = false;
                }
                i++;
                char Encrypted = (char)(c * i);
                Password += Encrypted.ToString();
            }
            form = (Username+Environment.NewLine + Email+ Environment.NewLine + Password);
            System.IO.File.WriteAllText(@"C://UnityTestFolder/" + Username + ".txt", form);
            userName.GetComponent<InputField>().text = "";
            email.GetComponent<InputField>().text = "";
            password.GetComponent<InputField>().text = "";
            confirmPassword.GetComponent<InputField>().text = "";
            print("Registration Successful!");
        }
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Tab))
        {
            if (userName.GetComponent<InputField>().isFocused) {
                email.GetComponent<InputField>().Select();
            }
            if (email.GetComponent<InputField>().isFocused)
            {
                password.GetComponent<InputField>().Select();
            }
            if (password.GetComponent<InputField>().isFocused)
            {
                confirmPassword.GetComponent<InputField>().Select();
            }
        }
        if (Input.GetKeyDown(KeyCode.Return)) {
            if(Username != "" && Email != "" && Password != "" && ConfPassword != "")
            {
                RegisterButton();
            }
        }
        Username = userName.GetComponent<InputField>().text;
        Email = email.GetComponent<InputField>().text;
        Password = password.GetComponent<InputField>().text;
        ConfPassword = confirmPassword.GetComponent<InputField>().text;

    }
    //Checks if email is valid
    void EmailValidation()
    {
        bool SW = false;
        bool EW = false;
        for(int i = 0; i < Characters.Length; i++)
        {
            if (Email.StartsWith(Characters[i]))
            {
                SW = true;
            }
        }
        for (int i = 0; i < Characters.Length; i++)
        {
            if (Email.EndsWith(Characters[i]))
            {
                EW = true;
            }
        }
        if(SW == true && EW == true)
        {
            EmailValid = true;
        }
        else
        {
            EmailValid = false;
        }
    }
}
