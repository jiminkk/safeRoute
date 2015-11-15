//
//  MapTasks.swift
//  GMapsDemo
//
//  Created by Nandini  on 11/14/15.
//  Copyright © 2015 Appcoda. All rights reserved.
//

import Foundation

class MapTasks {
    
    func httpPost (postsEndpoint: String, origin: String, destination: String) {
        guard let postsURL = NSURL(string: postsEndpoint) else {
            print("Error: cannot create URL")
            return
        }
        let postsUrlRequest = NSMutableURLRequest(URL: postsURL)
        postsUrlRequest.HTTPMethod = "POST"
        
        let newPost: NSDictionary = ["Origin": origin, "Destination": destination]
        do {
            let jsonPost = try NSJSONSerialization.dataWithJSONObject(newPost, options: [])
            postsUrlRequest.HTTPBody = jsonPost
            
            let config = NSURLSessionConfiguration.defaultSessionConfiguration()
            let session = NSURLSession(configuration: config)
            
            let task = session.dataTaskWithRequest(postsUrlRequest, completionHandler: {
                (data, response, error) in
                guard let responseData = data else {
                    print("Error: did not receive data")
                    return
                }
                guard error == nil else {
                    print("error calling GET on /posts/1")
                    print(error)
                    return
                }
                
                // parse the result as JSON, since that's what the API provides
                let post: NSDictionary
                do {
                    post = try NSJSONSerialization.JSONObjectWithData(responseData,
                        options: []) as! NSDictionary
                } catch  {
                    print("error parsing response from POST on /posts")
                    return
                }
                // now we have the post, let's just print it to prove we can access it
                print("The post is: " + post.description)
                
                // the post object is a dictionary
                // so we just access the title using the "title" key
                // so check for a title and print it if we have one

            })
            task.resume()
            
        } catch {
            print("Error: cannot create JSON from post")
        }
    }
}

