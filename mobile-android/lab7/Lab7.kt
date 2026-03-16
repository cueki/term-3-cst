package com.example.lab7

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.animation.animateContentSize
import androidx.compose.foundation.Image
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.lab7.ui.theme.Lab7Theme

/**
 * Madison Lovett, A01292253
 */

data class CharacterTile(val name: String, val imageRes: Int)

val allCharacters = listOf(
    CharacterTile("Ahsoka", R.drawable.ahsoka),
    CharacterTile("BB-8", R.drawable.bb8),
    CharacterTile("C-3PO", R.drawable.c3po),
    CharacterTile("Chewbacca", R.drawable.chewbacca),
    CharacterTile("Grogu", R.drawable.grogu),
    CharacterTile("Jabba", R.drawable.jabba),
    CharacterTile("Kylo", R.drawable.kilo),
    CharacterTile("Trooper", R.drawable.trooper),
    CharacterTile("Yoda", R.drawable.yoda),
)

class Lab7 : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            Lab7Theme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    TileScreen(modifier = Modifier.padding(innerPadding))
                }
            }
        }
    }
}

@Composable
fun TileScreen(modifier: Modifier = Modifier) {
    var shuffleKey by remember { mutableIntStateOf(0) }

    val rows = remember(shuffleKey) {
        allCharacters.shuffled().chunked(3)
    }

    Column(
        modifier = modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .padding(top = 16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Button(
            onClick = { shuffleKey++ },
            shape = RoundedCornerShape(4.dp)
        ) {
            Text("Shuffle")
        }

        rows.forEach { rowItems ->
            LazyRow(
                modifier = Modifier.padding(top = 12.dp),
                contentPadding = PaddingValues(horizontal = 16.dp),
                horizontalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                items(rowItems, key = { it.name }) { character ->
                    CharacterCard(character)
                }
            }
        }
    }
}

@Composable
fun CharacterCard(character: CharacterTile) {
    var expanded by remember { mutableStateOf(false) }
    val cardSize = if (expanded) 337.dp else 225.dp

    Card(
        shape = RoundedCornerShape(12.dp),
        elevation = CardDefaults.cardElevation(defaultElevation = 4.dp),
        modifier = Modifier
            .size(cardSize)
            .animateContentSize()
            .clickable { expanded = !expanded }
    ) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            modifier = Modifier.fillMaxSize()
        ) {
            if (!expanded) {
                Text(
                    text = character.name,
                    style = MaterialTheme.typography.titleLarge,
                    fontWeight = FontWeight.Bold,
                    modifier = Modifier.padding(8.dp)
                )
            }
            Image(
                painter = painterResource(id = character.imageRes),
                contentDescription = character.name,
                contentScale = ContentScale.Fit,
                modifier = Modifier
                    .fillMaxWidth()
                    .weight(1f)
            )
        }
    }
}

@Preview(showBackground = true)
@Composable
fun TileScreenPreview() {
    Lab7Theme {
        TileScreen()
    }
}
