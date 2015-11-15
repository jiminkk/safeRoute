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

    @IBOutlet weak var viewMap: GMSMapView!
    
    @IBOutlet weak var bbFindAddress: UIBarButtonItem!
    
    @IBOutlet weak var lblInfo: UILabel!
    
    var routeString: String!
    
    var routePolyline: GMSPolyline!
    
    let mapTasks = MapTasks!()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        
        //TODO: by calling createRoute, get origin and destination string from user, replace "Westwood", "Hollywood" with those (must be exact addr!)
        
        //Http POST request to flask server
        //returns json containing lowest-crime-index route (plus metadata)

        //mapTasks.httpPost("http://jsonplaceholder.typicode.com/posts", origin: "Westwood", destination: "Hollywood");
        routeString = mapTasks.httpPost("http://saferoute.azurewebsites.net/addresses", origin: "Westwood", destination: "Hollywood");
        //routeString = "ic}nErb~qUpBeCfGsGpAqBx@}@dByAz@iAHOPk@rBh@fATl@F|Hp@hD_AHG~DeDbFcE`BsAHE]aBc@_Cs@{EKa@uJwA"
        print(routeString)
        
        //Map view
        
        let camera = GMSCameraPosition.cameraWithLatitude(34.0500,
            longitude: -118.2500, zoom: 5)
        let mapView = GMSMapView.mapWithFrame(CGRectZero, camera: camera)
        mapView.myLocationEnabled = true
        self.view = mapView
        
        //TODO: remove this, and instaed call createRoute
        drawRoute()
        
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
       /* let addressAlert = UIAlertController(title: "Address Finder", message: "Destination:", preferredStyle: UIAlertControllerStyle.Alert)
        
        addressAlert.addTextFieldWithConfigurationHandler { (textField) -> Void in
            textField.placeholder = "Address?"
        }
        
        let findAction = UIAlertAction(title: "Find Address", style: UIAlertActionStyle.Default) { (alertAction) -> Void in
            let address = (addressAlert.textFields![0] as UITextField).text! as String
            
            self.mapTasks.geocodeAddress(address, withCompletionHandler: { (status, success) -> Void in
                
            })
            
        }
        
        let closeAction = UIAlertAction(title: "Close", style: UIAlertActionStyle.Cancel) { (alertAction) -> Void in
            
        }
        
        addressAlert.addAction(findAction)
        addressAlert.addAction(closeAction)
        
        presentViewController(addressAlert, animated: true, completion: nil)
*/
    }
    
    
    @IBAction func createRoute(sender: AnyObject) {
    
    }
    
    func drawRoute() {
        let path: GMSPath = GMSPath(fromEncodedPath: routeString) //exc_bad_instruction code=exc_1386
        routePolyline = GMSPolyline(path: path)
        routePolyline.map = viewMap
    }
    
    
    @IBAction func changeTravelMode(sender: AnyObject) {
    
    }
    
    
}

