import 'package:flutter/material.dart';
import 'package:smooth_page_indicator/smooth_page_indicator.dart';

void main() {
  runApp(MyApp());
}

int currentIndexPage = 0;

final _pageViewController =  PageController(
  initialPage: 0,
);

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  _onPageViewChange (int x) {setState(() {
    currentIndexPage = x;
  });}
  @override
  Widget build(BuildContext Context) {
    return MaterialApp(
      theme: ThemeData(
        primaryColor: Colors.white
      ),
      home: Scaffold(
        floatingActionButton: Container(
          height: 60.0,
          width: 380.0,
          child: SizedBox(
            child: FloatingActionButton(
              onPressed: () {},
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular((10))),
              backgroundColor: Colors.deepPurpleAccent[400],
              child: new Text("Create an account", style: TextStyle(fontSize: 18)),
            ),
          ),
        ),
        floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
        body: Stack(
            children: <Widget>[PageView(
            children: <Widget>[
              Container(
                child: Image(
                  image: AssetImage('assets/images/art-cloud.jpg')
                    )
                  ),
            Container(
              child: Image(
                image: AssetImage('assets/images/art-stairs.jpg')
              ),
            ),
          ],
              controller: _pageViewController,
              onPageChanged: _onPageViewChange,
          //scrollDirection: Axis.horizontal,
          //physics: BouncingScrollPhysics(),
        ),
            Align(
                alignment: Alignment.topCenter,
                child: Container(
                  padding: EdgeInsets.all(50.0),
                    child: SmoothPageIndicator(
                      controller: _pageViewController,
                      count: 2,
                      effect: ExpandingDotsEffect(
                        expansionFactor: 13,
                        dotWidth: 10.0,
                        dotHeight: 10.0,
                        activeDotColor: Colors.deepPurpleAccent[400],
                      ),
                    )
                )
              )
        ]
        )
      ),
    );
  }    }  // MyApp Class
