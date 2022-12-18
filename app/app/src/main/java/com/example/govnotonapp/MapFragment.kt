package com.example.govnotonapp

import android.app.Activity
import android.app.AlertDialog
import android.content.Context
import android.content.DialogInterface
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import com.example.govnotonapp.models.*
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.GoogleMap.OnInfoWindowClickListener
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.SupportMapFragment
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.Marker
import com.google.android.gms.maps.model.MarkerOptions
import com.google.android.material.snackbar.Snackbar

class MapFragment : Fragment(), OnMapReadyCallback {

    private lateinit var mMap: GoogleMap
    private lateinit var activity: Activity
    private lateinit var reportsFBParser: ReportsFBParser

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onAttach(activity: Activity) {
        this.activity = activity
        reportsFBParser = ReportsFBParser()
        super.onAttach(activity)
    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view: View = inflater.inflate(R.layout.fragment_map, container, false)

        reports = ArrayList()

        val mapFragment =
            childFragmentManager.findFragmentById(R.id.mapFragment_gMap) as SupportMapFragment
        if (mapFragment != null) {
            mapFragment.getMapAsync(this)
            // Toast.makeText(activity, "123", Toast.LENGTH_SHORT).show()
            Snackbar.make(view, "Map loaded successfully", Snackbar.LENGTH_LONG).show()
        } else {
            Snackbar.make(view, "Map loading error.", Snackbar.LENGTH_LONG).show()
        }
        return view
    }

    override fun onMapReady(googleMap: GoogleMap) {
        mMap = googleMap
        var almaty = LatLng(43.23076335448614, 76.91796490686353)
        //mMap.addMarker(MarkerOptions().position(almaty).title("Marker in Almaty"))
        mMap.moveCamera(CameraUpdateFactory.newLatLng(almaty))
        addMarkers(mMap)
        mMap.setInfoWindowAdapter(MarkerInfoWindowAdapter(activity))
        mMap.setOnInfoWindowClickListener {
            var report: Report
            report = it.tag as Report // getting report by clicking on pop-up window
            // Toast.makeText(activity, report.title, Toast.LENGTH_LONG).show()
            var builder = AlertDialog.Builder(activity)
            builder.setTitle("Choose an action:")
            builder.setNeutralButton("Cancel") { dialog, which ->
                Toast.makeText(activity, "Cancelled", Toast.LENGTH_SHORT).show()
                dialog.dismiss()
            }

            builder.setPositiveButton("Take"){
                dialog, which ->
                dialog.dismiss()
                val act = activity as MainActivity
                var builder2 = AlertDialog.Builder(act)
                builder2.setTitle("Please confirm:")
                builder2.setNeutralButton("Cancel"){
                    dialog1, which ->
                    Toast.makeText(activity, "Cancelled", Toast.LENGTH_SHORT).show()
                    dialog1.dismiss()
                }
                builder2.setPositiveButton("Confirm"){
                    dialog1, which ->
                    Toast.makeText(activity, "Taken", Toast.LENGTH_SHORT).show()
                    dialog1.dismiss()
                    act.switchToChatFragment()
                }
                builder2.show()
            }
            builder.show()
        }
    }

    private lateinit var reports: ArrayList<Report>

    fun getReports():ArrayList<Report>{
        return reports
    }


    private fun addMarkers(googleMap: GoogleMap) {
        var listener: OnReportsRetrievedListener = object : OnReportsRetrievedListener {
            override fun retrieveReports(array: ArrayList<Report>){
                reports.clear()
                reports.addAll(array)
                reports.forEach { report: Report ->
                    val marker = googleMap.addMarker(
                        MarkerOptions().position(report.convertLocationToLatLng(report.location))
                            .title(report.title)
                    )
                    if (marker != null) {
                        marker.tag = report
                    }
                    //  var x = report.location.indexOf(',')
                    // Toast.makeText(activity.applicationContext, report.location.substring(x+1), Toast.LENGTH_SHORT).show()
                }
            }
        }
        reportsFBParser.getReports(activity, listener)
        // reports = ReportParser(activity).parse(listener)
    }


}
