package com.example.bedrockapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class BreakInActivity extends AppCompatActivity {

    String phoneNumber = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_break_in);

        Intent intent = getIntent();
        phoneNumber = intent.getStringExtra("EXTRA_PHONE");
        textDoctor();
    }

    public void textDoctor() {

    }
}
