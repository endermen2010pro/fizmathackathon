package com.example.govnotonapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import com.google.android.material.bottomnavigation.BottomNavigationView
import com.google.android.material.snackbar.Snackbar

class MainActivity : AppCompatActivity() {

    lateinit var bottomNav: BottomNavigationView
    lateinit var mapFragment: MapFragment
    lateinit var chatsFragment: ChatsFragment
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        // declarations:
        mapFragment = MapFragment()
        chatsFragment = ChatsFragment()
        bottomNav = findViewById<BottomNavigationView>(R.id.bottom_nav)
        //
        loadFragment(mapFragment)
        //
        bottomNav.setOnItemSelectedListener {
            when (it.itemId) {
                R.id.bottom_nav_map ->{
                    loadFragment(mapFragment)
                    true
                }
                R.id.bottom_nav_chats ->{
                    loadFragment(chatsFragment)
                    true
                }
                else -> {
                    Snackbar.make(findViewById(R.id.fragment_container), "Unexpected error", Snackbar.LENGTH_SHORT).show()
                    true
                }
            }
        }
    }

    private fun loadFragment(fragment: Fragment) {
        val trans = supportFragmentManager.beginTransaction()
        trans.replace(R.id.fragment_container, fragment)
        trans.commit()
    }
}