package com.example.govnotonapp.models

import android.content.Context
import android.graphics.Color
import android.view.LayoutInflater
import android.view.View
import android.widget.TextView
import com.example.govnotonapp.R
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.model.Marker

class MarkerInfoWindowAdapter(private val context:Context): GoogleMap.InfoWindowAdapter {
    override fun getInfoContents(marker: Marker): View? {
        val report = marker.tag as? Report ?: return null
        val view = LayoutInflater.from(context).inflate(
            R.layout.marker_content, null
        )
        view.findViewById<TextView>(R.id.marker_tv_title).text = report.title.toString()
        view.findViewById<TextView>(R.id.marker_tv_body).text = report.body.toString()

        var bool: Boolean = report.isAccepted
        when(bool){
            false -> {
                view.findViewById<TextView>(R.id.marker_tv_status).text = "Unresolved"
                view.findViewById<TextView>(R.id.marker_tv_status).setTextColor(Color.parseColor("#F31212"))
            }
            true -> {
                view.findViewById<TextView>(R.id.marker_tv_status).text = "Pending"
                view.findViewById<TextView>(R.id.marker_tv_status).setTextColor(Color.parseColor("F7C414"))
            }
        }
        return view
    }

    override fun getInfoWindow(marker: Marker): View? {
        return null
    }

}