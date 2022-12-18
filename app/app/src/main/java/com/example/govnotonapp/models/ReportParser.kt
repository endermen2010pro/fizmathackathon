package com.example.govnotonapp.models

import android.content.Context
import android.widget.Toast
import org.json.*


class ReportParser(ctx: Context) {
    private var ctx: Context = ctx
    private var str =
        "{\"reports\": [{\"title\": \"Go\", \"location\": \"43.2304,76.918129\", \"body\": \"Bob\", \"image\": \"https://api.telegram.org/file/bot5542693067:AAGwMJoM5WgrwGWQQVJ20DpJERFUZSpHRFU/photos/file_52.jpg\", \"isAccepted\": \"false\"}, {\"title\": \"\\u0410\\u043f\\u043f\", \"location\": \"43.232444,76.917218\", \"body\": \"\\u041f\\u043e\\u043f\", \"image\": \"https://api.telegram.org/file/bot5542693067:AAGwMJoM5WgrwGWQQVJ20DpJERFUZSpHRFU/photos/file_52.jpg\", \"isAccepted\": \"false\"}, {\"title\": \"123\", \"location\": \"43.232428,76.917125\", \"body\": \"123\", \"image\": \"https://api.telegram.org/file/bot5542693067:AAGwMJoM5WgrwGWQQVJ20DpJERFUZSpHRFU/photos/file_57.jpg\", \"isAccepted\": \"false\"}, {\"title\": \"\\u041f\\u043e\", \"location\": \"43.232449,76.917249\", \"body\": \"\\u0418\\u043e\\u0448\", \"image\": \"https://api.telegram.org/file/bot5542693067:AAGwMJoM5WgrwGWQQVJ20DpJERFUZSpHRFU/photos/file_58.jpg\", \"isAccepted\": \"false\"}, {\"title\": \"\\u0412\\u0430\\u0440\\u0433\", \"location\": \"43.232432,76.917286\", \"body\": \"\\u041c\\u043e\\u043b\", \"image\": \"https://api.telegram.org/file/bot5542693067:AAGwMJoM5WgrwGWQQVJ20DpJERFUZSpHRFU/photos/file_59.jpg\", \"isAccepted\": \"false\"}]}"

    //TODO:
    /*
    Create a parsing method to parse data from firebase to string to JSON
     */
    // var obj: JSONArray = JSONArray(str)
    fun parse(string: String): ArrayList<Report> {
        try {
            var reportArrayList = ArrayList<Report>()
            var reports: JSONObject = JSONObject(string)
            var reportsArray: JSONArray = reports.getJSONArray("reports")
            for(i in 1 until reportsArray.length()){
                var obj = reportsArray.get(i) as JSONObject
                var title = obj.getString("title") // получаю тайтл как строку
                var location = obj.getString("location")
                var body = obj.getString("body")
                var image = obj.getString("image")
                var isAccepted = obj.getBoolean("isAccepted")
                var report: Report = Report(title,location,body,image,isAccepted)
                reportArrayList.add(report)
                // Toast.makeText(ctx, title, Toast.LENGTH_SHORT).show()
            }
            return reportArrayList
        } catch (e: java.lang.Exception) {
            Toast.makeText(ctx, "Unexpected error", Toast.LENGTH_SHORT).show()
            e.printStackTrace()
            var reportArrayList = ArrayList<Report>() // empty
            return reportArrayList
        }
    }

    fun parse(): ArrayList<Report> {
        try {
            var reportArrayList = ArrayList<Report>()
            var reports: JSONObject = JSONObject(str)
            var reportsArray: JSONArray = reports.getJSONArray("reports")
            for(i in 1 until reportsArray.length()){
                var obj = reportsArray.get(i) as JSONObject
                var title = obj.getString("title") // получаю тайтл как строку
                var location = obj.getString("location")
                var body = obj.getString("body")
                var image = obj.getString("image")
                var isAccepted = obj.getBoolean("isAccepted")
                var report: Report = Report(title,location,body,image,isAccepted)
                reportArrayList.add(report)
                // Toast.makeText(ctx, title, Toast.LENGTH_SHORT).show()
            }
            return reportArrayList
        } catch (e: java.lang.Exception) {
            Toast.makeText(ctx, "Unexpected error", Toast.LENGTH_SHORT).show()
            e.printStackTrace()
            var reportArrayList = ArrayList<Report>() // empty
            return reportArrayList
        }
    }
}