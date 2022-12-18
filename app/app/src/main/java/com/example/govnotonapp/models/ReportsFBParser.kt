package com.example.govnotonapp.models

import android.content.Context
import android.provider.ContactsContract.Data
import android.widget.Toast
import com.google.firebase.database.*
import com.google.firebase.database.core.Repo

class ReportsFBParser {
    val db: FirebaseDatabase = FirebaseDatabase.getInstance()
    val reports: DatabaseReference = db.reference.child("reports")


    fun getReports(ctx: Context, listener: OnReportsRetrievedListener) {
        var reportArray: ArrayList<Report> = ArrayList<Report>()
        var query: Query = reports
        query.addValueEventListener(object : ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {
                var reportsJSON: String = ""
                reportsJSON = snapshot.getValue(String::class.java).toString()
                /*for (data: DataSnapshot in snapshot.children) {
                    reportsJSON = data.getValue(String::class.java).toString()
                    var parser = ReportParser(ctx)
                    Toast.makeText(ctx, reportsJSON, Toast.LENGTH_SHORT).show()
                    reportArray = parser.parse(reportsJSON)
                    Toast.makeText(ctx, reportsJSON, Toast.LENGTH_SHORT).show()
                }*/
                var parser = ReportParser(ctx)
                reportArray = parser.parse(reportsJSON)
                Toast.makeText(ctx, reportsJSON, Toast.LENGTH_SHORT).show()
                listener.retrieveReports(reportArray)
            }

            override fun onCancelled(error: DatabaseError) {
                Toast.makeText(ctx, "Failed", Toast.LENGTH_SHORT).show()
            }
        })
    }

}