package com.example.govnotonapp.models

import android.net.Uri
import com.google.android.gms.maps.model.LatLng

class Report {
    lateinit var title: String
    lateinit var location: String
    lateinit var body: String
    lateinit var image: String
    lateinit var imageUri: Uri
    lateinit var positionLatLng: LatLng
    var isAccepted: Boolean = false

    constructor(title: String, location: String, body: String, image: String, isAccepted: Boolean){
        this.title = title
        this.location = location
        this.body = body
        this.image = image
        this.isAccepted = isAccepted
    }

    fun convertStringToUri(str: String){

    }
    //43.2304,76.918129
    fun convertLocationToLatLng(location: String):LatLng{
        var x = location.indexOf(',')
        var lat = location.substring(0,x).toDouble()
        var long = location.substring(x+1).toDouble()
        var latlng: LatLng = LatLng(lat, long)
        return latlng
    }
}