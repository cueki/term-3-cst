package com.example.lab6

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

/**
 * @author Madison Lovett
 */

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Lab6Layout()
        }
    }
}

@Preview(showBackground = true, showSystemUi = true)
@Composable
fun Lab6Layout() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color(0xFF608090))
            .padding(16.dp),
        verticalArrangement = Arrangement.SpaceBetween
    ) {
        Box {
            Box(
                modifier = Modifier
                    .width(180.dp)
                    .height(150.dp)
                    .background(Color(0xFF1030C0))
            )
            Box(
                modifier = Modifier
                    .padding(start = 160.dp, top = 120.dp)
                    .size(50.dp)
                    .background(Color(0xFFB00000))
            )
        }

        Row(
            modifier = Modifier
                .fillMaxWidth()
                .background(Color(0xFF8050D0))
                .padding(8.dp),
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Row(
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                Box(
                    modifier = Modifier
                        .size(80.dp)
                        .background(Color(0xFFE08080))
                )
                Box(
                    modifier = Modifier
                        .size(80.dp)
                        .background(Color(0xFF40A050))
                )
            }
            Box(
                modifier = Modifier
                    .size(100.dp)
                    .background(Color(0xFFE0C030))
            )
        }

        Box(
            modifier = Modifier
                .size(150.dp)
                .background(Color(0xFF805010))
                .align(Alignment.CenterHorizontally),
            contentAlignment = Alignment.Center
        ) {
            Text(
                text = "Lab 6",
                color = Color.White,
                fontSize = 28.sp
            )
        }
    }
}
