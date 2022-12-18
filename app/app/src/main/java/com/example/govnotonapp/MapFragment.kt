package com.example.govnotonapp

import android.app.Activity
import android.content.Context
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import com.example.govnotonapp.models.Report
import com.example.govnotonapp.models.ReportParser
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.SupportMapFragment
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions
import com.google.android.material.snackbar.Snackbar

class MapFragment : Fragment(), OnMapReadyCallback {

    private lateinit var mMap: GoogleMap
    private lateinit var activity: Activity
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onAttach(activity: Activity) {
        this.activity = activity
        super.onAttach(activity)
    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view: View = inflater.inflate(R.layout.fragment_map, container, false)
        val mapFragment =
            childFragmentManager.findFragmentById(R.id.mapFragment_gMap) as SupportMapFragment
        if (mapFragment != null) {
            mapFragment.getMapAsync(this)
            Snackbar.make(view, "Map loaded successfully", Snackbar.LENGTH_LONG).show()
        } else {
            Snackbar.make(view, "Map loading error.", Snackbar.LENGTH_LONG).show()
        }
        return view
    }

    override fun onMapReady(googleMap: GoogleMap) {
        mMap = googleMap
        var almaty = LatLng(43.23076335448614, 76.91796490686353)
        mMap.addMarker(MarkerOptions().position(almaty).title("Marker in Almaty"))
        mMap.moveCamera(CameraUpdateFactory.newLatLng(almaty))
        addMarkers(mMap)
    }

    private lateinit var reports: ArrayList<Report>
    private fun addMarkers(googleMap: GoogleMap) {
        reports = ReportParser(activity).parse()
        reports.forEach { report: Report ->
            val marker = googleMap.addMarker(
                MarkerOptions().position(report.convertLocationToLatLng(report.location)).title(report.title)
            )
            //  var x = report.location.indexOf(',')
            // Toast.makeText(activity.applicationContext, report.location.substring(x+1), Toast.LENGTH_SHORT).show()
        }
    }
}