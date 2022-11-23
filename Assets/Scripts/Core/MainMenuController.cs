using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenuController : MonoBehaviour
{
    public void PlayGameWithAI()
    {
        SceneManager.LoadScene("Game");
    }

    public void PlayGameOnline()
    {
        Debug.Log("Play with people");
    }
}
