let
    Source = Csv.Document(File.Contents("C:\Users\elton\projects\ai-data-copilot-pencil\powerbi\Student_Placement_Skills_2025_cleaned.csv"),[Delimiter=",", Columns=13, Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"Student_ID", Int64.Type},
        {"Gender", type text},
        {"Age", Int64.Type},
        {"Degree", type text},
        {"CGPA", type number},
        {"Internships_Count", Int64.Type},
        {"Projects_Count", Int64.Type},
        {"Certifications_Count", Int64.Type},
        {"Technical_Skills_Score_100", Int64.Type},
        {"Communication_Skills_Score_100", Int64.Type},
        {"Aptitude_Test_Score_100", Int64.Type},
        {"Placement_Offer", type text},
        {"Salary_Offered_USD", type number}
    }),
    CleanPlacement = Table.TransformColumns(ChangedTypes, {{"Placement_Offer", each Text.Trim(Text.Lower(_)), type text}}),
    PlacedFlag = Table.AddColumn(CleanPlacement, "Placed", each if [Placement_Offer] = "yes" then 1 else 0, Int64.Type)
in
    PlacedFlag
