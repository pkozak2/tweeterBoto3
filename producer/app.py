import json, boto3, uuid, time
sqs = boto3.resource('sqs', region_name='eu-central-1')
counter = 0
sendlatency = 0

tweets = sqs.get_queue_by_name(QueueName='pkozak')

while True:
 counterstr = str(counter)
 response = tweets.send_message(MessageBody='Message no:' + counterstr, MessageAttributes={
      'Author': {
          'StringValue': 'Piotr',
          'DataType': 'String'
      }
  })
 counter += 1
 sendlatency += 1
 if sendlatency == 50:
    print("waiting");
    time.sleep(15)
    sendlatency = 0

