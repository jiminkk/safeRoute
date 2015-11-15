//
//  ViewController.swift
//  GMapsDemo
//
//  Created by Gabriel Theodoropoulos on 29/3/15.
//  Copyright (c) 2015 Appcoda. All rights reserved.
//

import UIKit
import GoogleMaps

class ViewController: UIViewController {

    @IBOutlet weak var viewMap: UIView!
    
    @IBOutlet weak var bbFindAddress: UIBarButtonItem!
    
    @IBOutlet weak var lblInfo: UILabel!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        let mapTasks = MapTasks();
        
        //TODO: get origin and destination string from user, replace "Westwood", "Hollywood" with those (must be exact addr!)
        
        //Http POST request to flask server
        //returns json containing lowest-crime-index route (plus metadata)

        mapTasks.httpPost("http://jsonplaceholder.typicode.com/posts", origin: "Westwood", destination: "Hollywood");
        
        //TODO: make mapTasks function return a JSON (or dictionary using below code) instead of printing
        //Parse response json to create route
        //let dictionary: Dictionary<NSObject, AnyObject> = NSJSONSerialization.JSONObjectWithData(geocodingResultsData!, options: NSJSONReadingOptions.MutableContainers, error: &error) as Dictionary<NSObject, AnyObject>

        
        //Map view
        /*
        let camera = GMSCameraPosition.cameraWithLatitude(-33.86,
            longitude: 151.20, zoom: 6)
        let mapView = GMSMapView.mapWithFrame(CGRectZero, camera: camera)
        mapView.myLocationEnabled = true
        self.view = mapView
        */
        
        //let marker = GMSMarker()
        //marker.position = CLLocationCoordinate2DMake(-33.86, 151.20)
        //marker.title = "Sydney"
        //marker.snippet = "Australia"
        //marker.map = mapView
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


    // MARK: IBAction method implementation
    
    @IBAction func changeMapType(sender: AnyObject) {
        
    }
    
    
    @IBAction func findAddress(sender: AnyObject) {
    
    }
    
    
    @IBAction func createRoute(sender: AnyObject) {
    
    }
    
    
    @IBAction func changeTravelMode(sender: AnyObject) {
    
    }
    
    
}

