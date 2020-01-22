import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.ListIterator;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import javax.naming.Context;

public class UrlCount{


	public static class LinkGetter {  
		private Pattern htmltag;
		private Pattern link;

		public LinkGetter() {
			htmltag = Pattern.compile("<a\\b[^>]*href=\"[^>]*>(.*?)</a>");
			link = Pattern.compile("href=\"[^>]*\">");
		}

		public List<String> getLinks(String url) {
			List<String> links = new ArrayList<String>();
			try {
				Matcher tagmatch = htmltag.matcher(url);
				while (tagmatch.find()) {
					Matcher matcher = link.matcher(tagmatch.group());
					matcher.find();
					String link = matcher.group().replaceFirst("href=\"", "")
							.replaceFirst("\">", "")
							.replaceFirst("\"[\\s]?target=\"[a-zA-Z_0-9]*", "");
					if (valid(link)) {
						links.add(link);
					}
				}
			} catch(IllegalStateException e) {
				System.out.println(e);
			}
			return links;
		}


		private boolean valid(String s) {
			if (s.matches("javascript:.*|mailto:.*")) {
				return false;
			}
			return true;
		}
	}

	
	public static class UrlMapper extends Mapper<Object,Text,Text,IntWritable>{

		public void map(Object key, Text value, Context context) throws IOException, InterruptedException{
			
			UrlCount.LinkGetter links = new UrlCount.LinkGetter();
			List<String> urlList = links.getLinks(value.toString());
			HashMap<String,Integer> mappings = new HashMap<String,Integer>();

				for(int input =0; input< urlList.size();input++)
				{
					mappings.put(urlList.get(input) , (mappings.containsKey(urlList.get(input)))? mappings.get(urlList.get(input)) + 1 : 1);
				}

				for(String url : mappings.keySet())
				{

					Text t = new Text(url);
					IntWritable k = new IntWritable(mappings.get(url));
					context.write(t,k);
				}

		}
		
	}
	
	public static class UrlReducer extends Reducer<Text, IntWritable,Text,IntWritable>{

		public void reduce(Text url, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException{
			
			int sum = 0;
			for (IntWritable value: values) {
				sum += value.get();
			}
			IntWritable result = new IntWritable(sum);
			context.write(url,result);	
		}
	}

	public static void main(String[] args) throws Exception {
		
		Configuration conf = new Configuration();
	    Job job = Job.getInstance(conf, "count number of unique URLS");
	    job.setJarByClass(UrlCount.class);
	    job.setMapperClass(UrlMapper.class);
	    job.setCombinerClass(UrlReducer.class);
	    job.setReducerClass(UrlReducer.class);
	    job.setOutputKeyClass(Text.class);
	    job.setOutputValueClass(IntWritable.class);
	    FileInputFormat.addInputPath(job, new Path(args[0]));
	    FileOutputFormat.setOutputPath(job, new Path(args[1]));
	    System.exit(job.waitForCompletion(true) ? 0 : 1);
		
		

	}

}
