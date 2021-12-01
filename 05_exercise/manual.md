# BigQuery && Google Cloud SQL

- [BigQuery](https://cloud.google.com/bigquery)
- [What is BigQuery?](https://cloud.google.com/bigquery/docs/introduction)
- [BigQuery ecosystem intro](https://globalcloudplatforms.com/2021/08/11/query-big-with-bigquery-a-cheat-sheet/)

## BigQuery

0. Notice the BigQuery [pricing is related to MBs processed](https://cloud.google.com/bigquery/pricing).

1. Navigate to [cloud.google.com/bigquery/docs/quickstarts/quickstart-cloud-console](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-cloud-console).

2. Click "Go to Big Query".

3. Add dataset, search for `USA Name Data public dataset`.

4. Run the following query:

   ```sql
   SELECT
     name, gender,
     SUM(number) AS total
   FROM
     `bigquery-public-data.usa_names.usa_1910_2013`
   GROUP BY
     name, gender
   ORDER BY
     total DESC
   LIMIT 10
   ```

5. Let's now query another dataset - *github_repos*. Answer the following questions:

   - What are the github repos licenses?
   - What is the most popular license?

6. View the `languages` table. Is there something new here? Let's query the github dataset:

   ```sql
    SELECT t0.name, t0.repo_name FROM (
        SELECT repo_name, l.name
        FROM `bigquery-public-data.github_repos.languages` LEFT JOIN unnest(language) as l
        LIMIT 3000
    ) AS t0;
   ```

   What is the most popular programming language defined as programming language used in the most of the github repositories? 

7. Let's see how many commit subjects are the same:

   ```sql
   SELECT subject AS subject,
          COUNT(*) AS num_duplicates
   FROM `bigquery-public-data.github_repos.sample_commits`
   GROUP BY subject
   ORDER BY num_duplicates DESC
   LIMIT 100
   ```

8. You could also query the data about covid-19: `covid19_open_data`.

9. Notice, you can query BigQuery from [Google Spreadsheet](./spreadsheet.js) or [Google Data Studio](https://datastudio.google.com/).

## Google Cloud SQL

What are the benefits of the hosted database?

## AWS DynamoDB

[NoSQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-general-nosql-design.html), [eventual consistent](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html), and global scale database:

- [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)
- [DynamoDB Tutorial](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html)

## BigQuery - from ETL to ELT

<img src="https://miro.medium.com/max/1400/0*fJEKULbHVSe14xD2" width="45%" />
<!-- https://blog.rittmananalytics.com/how-rittman-analytics-centralizes-saas-data-sources-using-dbt-and-google-bigquery-3fd952773ec1 -->

[dbt](https://github.com/dbt-labs/dbt-core) is a tool often use for ELT.

## References

- [BigQuery DML](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax)
- [BigQuery best practices costs](https://cloud.google.com/bigquery/docs/best-practices-costs)
- [Blog post on querying github data from BigQuery](https://medium.com/nerd-for-tech/yet-another-analysis-of-bigquery-github-dataset-3be93c0857ff)
- [dbt](https://github.com/dbt-labs/dbt-core) - tool for transforming data after it is loaded to the warehouse
- [dbt tutorial](https://github.com/josephmachado/simple_dbt_project)
