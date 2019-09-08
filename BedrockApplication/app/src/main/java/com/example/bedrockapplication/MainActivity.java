package com.example.bedrockapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Timer;
import java.util.TimerTask;


public class MainActivity extends AppCompatActivity {

    private String phoneNumber = "";

    EditText phone;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        phone = (EditText) findViewById(R.id.phone_number_edit);

        Timer t = new Timer();
        t.schedule(new TimerTask() {

            public void run() {
                try {
                    URL url = new URL("http://10.251.90.88:5000/checkAlive/");
                    HttpURLConnection con = (HttpURLConnection) url.openConnection();
                    con.setRequestMethod("GET");

                    BufferedReader in = new BufferedReader(
                            new InputStreamReader(con.getInputStream()));
                    String inputLine;
                    StringBuffer content = new StringBuffer();
                    while ((inputLine = in.readLine()) != null) {
                        content.append(inputLine);
                    }
                    in.close();
                    con.disconnect();

                    if(content.toString().equals("Dead")) {
                        onBreakIn();
                    }
                } catch(Exception e) {
                    Log.d("MainActivity", e.toString());
                }

            }
        }, 1000);
    }



    public void onBreakIn() {
        Intent intent = new Intent(this, BreakInActivity.class);
        intent.putExtra("EXTRA_PHONE", phoneNumber);
        startActivity(intent);
    }

    public void confirmPhone(View view) {
        phoneNumber = phone.getText().toString();
        Toast.makeText(this, "Phone Number Confirmed", Toast.LENGTH_SHORT).show();
    }

    public void sendDispense(View view) {
        try {
            URL url = new URL("http://10.251.90.88:5000/sendDispense/");
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");
            con.disconnect();
        } catch(Exception e) {
            Log.d("Main Activity", e.toString());
        }
    }
}