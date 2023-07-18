using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Tracking : MonoBehaviour
{
    public Receive receive;
    public GameObject obj;
   // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        string data = receive.data;
        if(data.Length>=2) 
        {
            data = data.Substring(1, data.Length - 2);
            print(data);
            string [] coor = data.Split(',');
            float x = float.Parse(coor[0]);
            float y = float.Parse(coor[1]);
            print(x);
            print(y);
            x /= 100;
            y /= 100;
            x *= -1; y*= -1;
            obj.transform.position = new Vector3(x,y,0);
         }
        // string [] coor = data.Split(',');
        // print(coor[0]);


    }
}
