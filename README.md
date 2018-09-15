# Large Scale Instructional Design Analysis

## Updates
----

### 15<sup>th</sup> September, 2018

* Sequences with `Branching` involved have certain parameters such as `parentUIID`, `inputActivities`, `activityUIID`, `applyGrouping`, which can be used to create multiple branches
* `Aggregated Activities` house multiple activities, each of which are intialised with respect to the parent activity
* Example: There are 3 groups : Caterpillar, Lady Beetle, and Butterfly, in the sequence `australiasneighbours`.
* Each of these groups have `parentUIID` set to 19, viz. the `activityUIID` of `Branching` node.
* This means, that grouping is initialised in the `Branching` stage.
* This flows into the `Aggregation` called `Resources&Forums`
* There are other activities which we do not visually find on the sequence.
* These certain activities have a `parentUIID` which helps us to understand its origin.
* Branching (activityUIID = 19) &rarr; Caterpillar (activityUIID = 38, parentUIID = 19) &rarr; Qn'A (activityUIID = 42, parentUIID = 38)

-----

* Every learning sequence is stored in their zipped formats
* `tool.xml` per Activity, describes the inner workings of that Activity
* `learning_design.xml` is the main XML script which refer to the `tool.xml` scripts on the basis of `<ActivityID>` values

* `tool.xml` contains the serialized version of the authored graphs. The file is typically located under a sub-folder which bears the same name/ID as that of the `<toolContentId>` value. 
```
Format: <toolContentId>\tool.xml
Example: 1563\tool.xml
```

* `<transitions>` : Contains flow information per connection between activities
```
<transitions>
  <org.lamsfoundation.lams.learningdesign.dto.TransitionDTO>
    <transitionID>891</transitionID>
    <transitionUIID>9</transitionUIID>
    <toUIID>2</toUIID>
    <fromUIID>1</fromUIID>
    <createDateTime class="sql-timestamp">1970-01-01 11:00:00.0</createDateTime>
    <toActivityID>1349</toActivityID>
    <fromActivityID>1348</fromActivityID>
    <learningDesignID>98</learningDesignID>
  </org.lamsfoundation.lams.learningdesign.dto.TransitionDTO>
</transitions>
```
* `<validDesign>` : Parse script if the value is `true`
* `<createDateTime>` : Contains information on when sequence was created. Use this to parse scripts in chronological order
* `<activityCategoryID>` : ?
* `<activityTypeID>` : ?

# Questions

* Are the scripts aware regarding the category to which they belong to?
* How are the data stored in each activity node in the LAMS graphs, expressed in terms of XML? Where is that code block located in the scripts?
* Will XML parsing as Element Tree be the appropriate way to start off with? 
* Would converting them into UML via XSLT processor make it easier to work with later?
* Which would be better - general XML Parsing and scraping information OR treating the files as a corpus of text?
* How can we convert the XML scripts into Neo4J graphs via the Python Driver?
* What are the XML features which the model should take as input for processing?
* How can the model be trained on a very basic level to predict and suggest a suitable successor to any particular activity?

Ans. 
Assuming that the LAMS sequences are stored in XML formats, the model can take in a few features such as '<activityTitle>' viz. listed under '<activities>'. Every '<activityTitle>' has a unique '<activityUIID>' associated with it, which is later used by the '<transitions>' block to define connections between activities through '<fromUIID>' and '<toUIID>'. A tuple of the title and the ID can be used as a feature to train the model. Since, there are quite a few patterns which are widely used and are effective as well, the training phase can be handled accordingly.

* How to make sure that the suggested successor to an activity would prove to be impactful on learners? 

# LAMS Activities

<div align="center">
<img src="https://wiki.lamsfoundation.org/download/attachments/5570607/types.png?version=1&modificationDate=1260541901000"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px"/>
</div>
